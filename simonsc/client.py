#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import socket
import sys
import six
import threading
import time
import requests
from os import path
import pyarrow as pa

import msgpack
import thriftpy2 as thriftpy
from thriftpy2 import transport, protocol
if platform.system().lower() != "windows":
    socket_error = (transport.TTransportException, socket.error, protocol.cybin.ProtocolError)
else:
    socket_error = (transport.TTransportException, socket.error)
from thriftpy2.rpc import make_client

thrift_path = path.join(sys.modules["ROOT_DIR"], "simons.thrift")
thrift_path = path.abspath(thrift_path)
module_name = path.splitext(path.basename(thrift_path))[0]
thrift = None
with open(thrift_path) as f:
    simons_thrift = thriftpy.load_fp(f, "simons_thrift")
   

class SimonsClient(object):
    _threading_local = threading.local()
    _auth_params = {}

    @classmethod
    def instance(cls):
        _instance = getattr(cls._threading_local, '_instance', None)
        if _instance is None:
            if cls._auth_params:
                _instance = SimonsClient(**cls._auth_params)
            cls._threading_local._instance = _instance
        return _instance
    
    def __init__(self, host, port, username="", password="", retry_cnt=5):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.retry_cnt = retry_cnt
        self.inited = False
    
    @classmethod
    def set_auth_params(cls, **params):
        cls._auth_params = params
        cls.instance().ensure_auth()
    
    def ensure_auth(self):
        if not self.inited:
            if not self.username or not self.password:
                raise RuntimeError("not inited")
            
            try:
                self.client = make_client(simons_thrift.SimonsService, self.host, self.port, timeout=300000)
            except Exception as e:
                print(e)
            else:
                self.inited = True
            
            if self.username:
                response = self.client.auth(self.username, self.password)
            auth_message = response.msg
            if not sys.stdout.isatty():
                auth_message = ""
            if not response.status:
                self._threading_local._instance = None
                raise self.get_error(response)
            else:
                if self.not_auth:
                    print("auth success {}".format(auth_message))
                    self.not_auth = False
                    
    def _reset(self):
        if self.client:
            self.client.close()
            self.client = None
        self.inited = False
        self.http_token = ""

    def logout(self):
        self._reset()
        self._threading_local._instance = None
        self.__class__._auth_params = {}
        print("已退出")

    def get_error(self, response):
        err = None
        if six.PY2:
            system = platform.system().lower()
            if system == "windows":
                err = Exception(response.error.encode("gbk"))
            else:
                err = Exception(response.error.encode("utf-8"))
        else:
            err = Exception(response.error)
        return err

    def __call__(self, method, **kwargs):
        request = simons_thrift.St_Query_Req()
        request.method_name = method
        request.params = msgpack.packb(kwargs)
        err, result = None, None
        for idx in range(self.retry_cnt):
            try:
                file = six.BytesIO()
                self.ensure_auth()
                response = self.client.query(request)    
                if response.status:
                    returned_msg = response.msg
                    if six.PY3:
                        if isinstance(returned_msg, bytes):
                            buffer = pa.py_buffer(returned_msg)
                            result = pa.deserialize(buffer)
                else:
                    err = self.get_error(response)
                break 
            except KeyboardInterrupt as e:
                self._reset()
                err = e
                raise
            except socket_error as e:
                self._reset()
                err = e
                # time.sleep(1)  # # time.sleep(idx)
                continue
            except Exception as e:
                self._reset()
                err = e
                break
            finally:
                file.close()

        if result is None:
            if isinstance(err, Exception):
                raise err

        return result

    def __getattr__(self, method):
        return lambda **kwargs: self(method, **kwargs)
            