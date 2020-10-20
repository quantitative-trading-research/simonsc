#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from simonsc import auth
from simonsc.api import all_instruments, history_bars, history_snapshot

auth("quantresearch","quantresearch") 

# test history_bars one company
dt = pd.Timestamp("2019-03-28 14:57:00")
fields=["datetime","open","high","low","close"]
data = history_bars(order_book_ids="000001.XSHE", dt=dt, bar_count=10, frequency="1m", fields=fields)
print(data)

# test history_bars multiple companies
dt = datetime.datetime(2020,4,20,0,0,0)
fields=["datetime","open","high","low","close","volume"]
order_book_list = ['000001.XSHE', '000002.XSHE', '600000.XSHE']
data = history_bars(order_book_ids =order_book_list, dt=dt, bar_count=10, frequency="1d", fields=fields)
print(data)

# test history_snapshot
dt = pd.Timestamp("2020-07-24 14:55:00")
fields=["datetime","last","buy_price_1","buy_volume_1","sell_price_1","sell_volume_1","sell_price_10"]
data = history_snapshot(order_book_id="600446.XSHG", dt=dt, bar_count=10, fields=fields)
print(data)