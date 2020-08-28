#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import six
import datetime
import pandas as pd
from functools import wraps


def assert_auth(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):        
        from .client import SimonsClient
        if not SimonsClient.instance():
            print("run simonsc.auth first")
        else:
            return func(*args, **kwargs)
    return _wrapper

def convert_datetime_to_str(dt):
    if dt is None:
        return None
    if isinstance(dt, pd.Timestamp):
        dt = dt.to_pydatetime()
    if isinstance(dt, six.string_types):
        return dt
    if isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(dt, datetime.date):
        return dt.strftime("%Y-%m-%d")