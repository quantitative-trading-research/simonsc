#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from simonsc import auth
from simonsc.api import history_snapshot

auth("quantresearch","quantresearch")        
dt = pd.Timestamp("2020-07-24 14:55:00")
fields=["datetime","last","buy_price_1","buy_volume_1","sell_price_1","sell_volume_1","sell_price_10"]
data = history_snapshot(order_book_id="600446.XSHG", dt=dt, bar_count=10, fields=fields)
print(data)