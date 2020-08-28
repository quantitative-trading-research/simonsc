#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.modules["ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))

from .api import *
from .client import SimonsClient

def auth(username, password, host='10.202.33.83', port=6000):
    SimonsClient.set_auth_params(host=host, port=port, username=username, password=password)
    
    


