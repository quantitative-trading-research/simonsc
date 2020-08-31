#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List, Union
import datetime 
import numpy as np
import pandas as pd
from simonsc.client import SimonsClient
from simonsc.utils import *


__all__ = []

@assert_auth
@export_as_api
def get_trading_dates(start_date: Union[str, datetime.date, datetime.datetime, pd.Timestamp], end_date: Union[str, datetime.date, datetime.datetime, pd.Timestamp]) -> pd.DatetimeIndex:
    """
    获取A股某个区间的交易日期
    :param start_date: 开始日期
    :param end_date: 结束如期
    
    Example::
    
    获取2020-05-10至2020-05-20之间的交易日期
    
    ..  code-block:: python3
        
        from simonsc.api import get_trading_dates
    
        # 
        >>> trading_dates = get_trading_dates(start_date = "2020-05-11", end_date="2020-05-20")
        >>> print(trading_dates)
        DatetimeIndex(['2020-05-11', '2020-05-12', '2020-05-13', '2020-05-14',
               '2020-05-15', '2020-05-18', '2020-05-19', '2020-05-20'],
              dtype='datetime64[ns]', freq=None)
    """
    start_date = convert_datetime_to_str(start_date)
    end_date = convert_datetime_to_str(end_date)
    return SimonsClient.instance().get_trading_dates(**locals())


@export_as_api
def get_previous_trading_date(date: Union[str, datetime.date, datetime.datetime, pd.Timestamp], n: int=1) -> pd.Timestamp:
    """
    获取指定日期的之前的第 n 个交易日
    
    :param date: 指定日期
    :param n: 第 n 个交易日
    
    Example::
       
    2020-05-18之前3天的交易日
    
    ..  code-block:: python3
    
        from simonsc.api import get_previous_trading_date
        
        >>> get_previous_trading_date(date='2020-05-18', n=3)
        Timestamp('2020-05-13 00:00:00')
    """
    date = convert_datetime_to_str(date)
    return SimonsClient.instance().get_previous_trading_date(**locals())


@export_as_api
def get_next_trading_date(date: Union[str, datetime.date, datetime.datetime, pd.Timestamp], n:int=1) -> pd.Timestamp:
    """
    获取指定日期之后的第 n 个交易日
    
    :param date: 指定日期
    :param n: 第 n 个交易日
        
    :example:
    
    ..  code-block:: python3
    
        from simonsc.api import get_next_trading_date
    
        >>> get_next_trading_date(date='2020-05-13', n=3)
        Timestamp('2020-05-18 00:00:00')
    """
    date = convert_datetime_to_str(date)
    return SimonsClient.instance().get_next_trading_date(**locals())
