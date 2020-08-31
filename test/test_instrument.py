#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import datetime

from simonsc import auth
from simonsc import all_instruments, get_instruments

auth("quantresearch","quantresearch")


data = all_instruments(type="CS")