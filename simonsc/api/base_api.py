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
def all_instruments(type: str=None, date: Union[str, datetime.datetime, datetime.date]=None) ->pd.DataFrame:
    """
    获取simons目前支持的所有合约信息
    
    :param type: 需要查询合约类型，例如：type='CS'代表股票。默认是所有类型
    :param date: 查询时间点
   
    其中type参数传入的合约类型和对应的解释如下 
  
    
    =========================   ====================================================
    合约类型                     说明
    =========================   ====================================================
     CS                           Common Stock, 即股票
     ETF                          Exchange Traded Fund, 即交易所交易基金
     LOF                          Listed Open-Ended Fund，即上市型开放式基金
     INDX                         Index, 即指数
     Future                       Futures，即期货，包含股指、国债和商品期货
    =========================   ====================================================    
    :example:
    
    .. code-block:: python3
        
        >>> instrument_df = all_instruments(type="CS")
        >>> instrument_df.head()
           order_book_id symbol industry_code exchange  status type listed_date
        0   000001.XSHE   平安银行           J66     XSHE  Active   CS  1991-04-03
        1   000002.XSHE    万科A           K70     XSHE  Active   CS  1991-01-29
        2   000004.XSHE   国农科技           I65     XSHE  Active   CS  1991-01-14
        3   000005.XSHE   世纪星源           N77     XSHE  Active   CS  1990-12-10
        4   000006.XSHE   深振业A           K70     XSHE  Active   CS  1992-04-27
    """
    date = convert_datetime_to_str(date)
    return SimonsClient.instance().all_instruments(**locals())


@assert_auth
@export_as_api
def history_bars(
    order_book_id: str,
    bar_count: int,
    frequency: str,
    dt: datetime.datetime,
    fields: List[str]=None,
    skip_suspended: bool=True,
    include_now: bool=False,
    adjust_type: str="pre",
    adjust_orig:datetime.datetime = None,
) -> np.ndarray:
    """获取指定合约的历史 k 线行情，支持任意日频率xd(1d,5d)和任意分钟频率xm(1m,3m,5m,15m)的历史数据。
    
    :param order_book_id: 合约代码
    :param bar_count: 获取的历史数据数量，必填项
    :param frequency: 获取数据什么样的频率进行。'1d'或'1m'分别表示每日和每分钟，必填项
    :param fields: 返回数据字段。必填项。见下方列表。
    :param skip_suspended: 是否跳过停牌数据
    :param include_now: 是否包含当前数据
    :param adjust_type: 复权类型，默认为前复权 pre；可选 pre, none, post
    =========================   ===================================================
    fields                      字段名
    =========================   ===================================================
    datetime                    时间戳
    open                        开盘价
    high                        最高价
    low                         最低价
    close                       收盘价
    volume                      成交量
    total_turnover              成交额
    open_interest               持仓量（期货专用）
    basis_spread                期现差（股指期货专用）
    settlement                  结算价（期货日线专用）
    prev_settlement             结算价（期货日线专用）
    =========================   ===================================================
    
    Example1::
    
    获取中国平安 2020-04-20之前10天的交易数据
    
    ..  code-block:: python3
        
        import pandas as pd
        from simonsc.api import history_bars
    
        # 
        >>> dt = pd.Timestamp("2020-04-20")
        >>> fields=["datetime","open","high","low","close"]
        >>> data = history_bars(order_book_id="000001.XSHE", dt=dt, bar_count=10, frequency="1d", fields=fields)
        >>> print(data)
        array([(20200407000000, 12.89, 12.94, 12.81, 12.88),
               (20200408000000, 12.88, 12.92, 12.72, 12.78),
               (20200409000000, 12.88, 12.89, 12.72, 12.74),
               (20200410000000, 12.76, 12.98, 12.65, 12.79),
               (20200413000000, 12.67, 12.71, 12.47, 12.59),
               (20200414000000, 12.65, 12.86, 12.57, 12.86),
               (20200415000000, 12.86, 12.93, 12.78, 12.87),
               (20200416000000, 12.79, 12.79, 12.54, 12.68),
               (20200417000000, 12.77, 13.04, 12.65, 12.89),
               (20200420000000, 12.86, 13.05, 12.77, 12.99)],
              dtype={'names':['datetime','open','high','low','close'], 'formats':['<i8','<f8','<f8','<f8','<f8'], 'offsets':[0,8,24,32,16], 'itemsize':72})
    
    Example2::
    
    获取中国平安 2019-03-28 14:57 之前9个1 minutes(1m)的交易数据
    
    ..  code-block:: python3
        
        import pandas as pd
        from simonsc.api import history_bars
    
        # 
        >>> dt = pd.Timestamp("2019-03-28 14:57:00")
        >>> fields=['datetime','open','high','low','close','volume','total_turnover']
        >>> data = history_bars(order_book_id="000001.XSHE", dt=dt, bar_count=10, frequency="1m", fields=fields)
        >>> print(data)
        array([(20190328144900, 11.87, 11.88, 11.87, 11.87, 289054., 3430976.),
               (20190328145000, 11.88, 11.88, 11.87, 11.87, 321434., 3815179.),
               (20190328145100, 11.87, 11.88, 11.87, 11.88, 306734., 3641216.),
               (20190328145200, 11.88, 11.89, 11.87, 11.87, 430703., 5116544.),
               (20190328145300, 11.89, 11.9 , 11.88, 11.88, 364401., 4333824.),
               (20190328145400, 11.88, 11.89, 11.88, 11.89, 129211., 1534715.),
               (20190328145500, 11.89, 11.89, 11.86, 11.87, 478399., 5681344.),
               (20190328145600, 11.86, 11.87, 11.85, 11.86, 482408., 5724352.),
               (20190328145700, 11.86, 11.87, 11.86, 11.87, 122735., 1456704.)],
              dtype={'names':['datetime','open','high','low','close','volume','total_turnover'], 'formats':['<i8','<f8','<f8','<f8','<f8','<f8','<f8'], 'offsets':[0,8,24,32,16,56,64], 'itemsize':72})
    
    Example3::
    
    获取中国平安 2019-03-28 14:57 之前9个5 minutes(5m)的交易数据
    
    ..  code-block:: python3
        
        import pandas as pd
        from simonsc.api import history_bars
    
        # 
        >>> dt = pd.Timestamp("2019-03-28 14:57:00")
        >>> fields=['datetime','open','high','low','close','volume','total_turnover']
        >>> data = history_bars(order_book_id="000001.XSHE", dt=dt, bar_count=10, frequency="5m", fields=fields)
        >>> print(data)
        array([(20190328141500, 11.88, 11.91, 11.88, 11.9 , 1029062., 12237508.),
               (20190328142000, 11.91, 11.92, 11.9 , 11.92, 1179858., 14049280.),
               (20190328142500, 11.91, 11.92, 11.88, 11.89,  908278., 10809083.),
               (20190328143000, 11.88, 11.89, 11.86, 11.89,  739698.,  8786307.),
               (20190328143500, 11.88, 11.92, 11.88, 11.9 , 1291285., 15366140.),
               (20190328144000, 11.9 , 11.91, 11.88, 11.89, 1336515., 15894273.),
               (20190328144500, 11.89, 11.92, 11.89, 11.91, 2163997., 25753086.),
               (20190328145000, 11.92, 11.92, 11.87, 11.87, 2137786., 25418699.),
               (20190328145500, 11.87, 11.9 , 11.86, 11.87, 1709448., 20307643.),
               (20190328145700, 11.86, 11.87, 11.85, 11.87,  605143.,  7181056.)],
              dtype=[('datetime', '<u8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'), ('volume', '<f8'), ('total_turnover', '<f8')])
    
    """
    dt = convert_datetime_to_str(dt)
    return SimonsClient.instance().history_bars(**locals())

