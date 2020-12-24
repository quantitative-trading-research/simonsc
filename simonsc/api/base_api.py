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
    order_book_ids: str,
    bar_count: int,
    frequency: str,
    dt: datetime.datetime,
    fields: List[str]=None,
    skip_suspended: bool=True,
    include_now: bool=False,
    adjust_type: str="pre",
    adjust_orig:datetime.datetime = None,
) -> pd.DataFrame:
    """获取指定合约的历史 k 线行情，支持任意日频率xd(1d,5d)和任意分钟频率xm(1m,3m,5m,15m)的历史数据。
    
    :param order_book_ids: 多个标的合约代码
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
    
    获取中国平安和万科 2020-04-20之前10天的交易数据
    
    ..  code-block:: python3
        
        import pandas as pd
        from simons.api import history_bars
    
        # 
        >>> dt = pd.Timestamp("2020-04-20")
        >>> fields=["datetime","open","high","low","close","volume"]
        >>> data = history_bars(order_book_ids=["000001.XSHE", "000002.XSHE"], dt=dt, bar_count=10, frequency="1d", fields=fields)
        >>> print(data)
        
                                       open   high    low  close     volume
        order_book_id datetime                                  
        000001.XSHE   2020-04-07      12.89  12.94  12.81  12.88    87031371.0
                      2020-04-08      12.88  12.92  12.72  12.78    52871614.0
                      2020-04-09      12.88  12.89  12.72  12.74    40855377.0
                      2020-04-10      12.76  12.98  12.65  12.79    66667495.0
                      2020-04-13      12.67  12.71  12.47  12.59    44621440.0
                      2020-04-14      12.65  12.86  12.57  12.86    68608687.0
                      2020-04-15      12.86  12.93  12.78  12.87    65639640.0
                      2020-04-16      12.79  12.79  12.54  12.68    78915498.0
                      2020-04-17      12.77  13.04  12.65  12.89   133116477.0
                      2020-04-20      12.86  13.05  12.77  12.99    81845583.0
        000002.XSHE   2020-04-07      27.34  27.42  26.80  27.07    67154006.0
                      2020-04-08      26.90  27.25  26.75  26.96    41251395.0
                      2020-04-09      27.10  27.16  26.60  26.69    38726254.0
                      2020-04-10      26.84  27.34  26.59  26.88    62460322.0
                      2020-04-13      26.74  27.13  26.61  27.04    43264902.0
                      2020-04-14      27.10  27.75  27.02  27.35    64241868.0
                      2020-04-15      27.20  27.23  26.55  26.70    70359257.0
                      2020-04-16      26.52  26.76  26.40  26.58    50238931.0
                      2020-04-17      26.78  27.03  26.55  26.72    83813322.0
                      2020-04-20      26.78  26.81  26.05  26.58    85012343.0
    
    """
    dt = convert_datetime_to_str(dt)
    return SimonsClient.instance().history_bars(**locals())


@assert_auth
@export_as_api
def history_snapshot(
    order_book_id: str,
    bar_count: int,
    dt: datetime.datetime,
    fields: List[str]=None,
    skip_suspended: bool=True,
    include_now: bool=False,
    adjust_type: str="none",
    adjust_orig:datetime = None,
) -> pd.DataFrame:
    """获取指定合约的历史快照数据
    
    :param order_book_id: 合约代码
    :param bar_count: 获取的历史数据数量，必填项
    :param fields: 返回数据字段。必填项。见下方列表。
    :param skip_suspended: 是否跳过停牌数据
    :param include_now: 是否包含当前数据
    :param adjust_type: 复权类型，默认为前复权 pre；可选 pre, none, post
    
    .. admonition:: 可支持的数据字段
        :class: dropdown, note
        
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | fields                                 | 中文名                   | dtype   | 是否是原始字段 |  注释                                                 |   
        +========================================+==========================+=========+================+=======================================================+
        | date                                   | 交易归属日期             | <i8     | Y              | yyyymmdd                                              |    
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | datetime                               | 交易发生时间             | <i8     | C              | yyyymmddhhmmss，由交易日当天日期和数据生成时间（交易s |
        |                                        |                          |         |                |（交易所直接下发的）合成。                             |       
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | last                                   | 最新成交价               | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | sell_price_10 ~ sell_price_1           | 第10 ~ 1档委托卖出价     | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | buy_price_1 ~ buy_price_10             | 第1 ~ 10档委托买入价     | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | sell_volume_10 ~ sell_volume_1         | 第10 ~ 1档申卖量         | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | buy_volume_1 ~ buy_volume_10           | 第1 ~ 10档申买量         | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | num_sell_trades_10 ~ num_sell_trades_1 | 委卖笔数10  ~  委卖笔数1 | <f8     | Y              | 委卖价1 ~ 10的委托总比数                              |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | num_buy_trades_1 ~ num_buy_trades_10   | 委买笔数1  ~  委买笔数10 | <f8     | Y              | 委买价1 ~ 10的委托总比数                              |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | total_num_trades                       | 成交总笔数               | <f8     | Y              | 开盘至当前时刻的累计成交笔数                          |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | current_num_trades                     | 分笔期间成交笔数         | <f8     | 上交所：N      | 当前成交总比数(total_num_trades_t) - 上一记录的成     |
        |                                        |                          |         | 深交所：Y      | 交总比数(total_num_trades_t-1);首条记录取当前成交     |
        |                                        |                          |         |                | 总比                                                  |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | total_volume                           | 成交总量                 | <f8     | Y              | 开盘至当前时刻的累计成交量                            |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | current_volume                         | 分笔期间成交量           | <f8     | 上交所：N      | 当前成交总量(total_volume_t ) - 上一记录的成          |
        |                                        |                          |         | 深交所：Y      | 交总量(total_volume_t-1);首条记录取当前成交总量       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | total_turnover                         | 成交总额                 | <f8     | Y              | 开盘至当前时刻的累计成交额                            |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | current_turnover                       | 分笔期间成交额           | <f8     | 上交所：N      | 当前成交总额(total_turnover_t) - 上一记录的成交总额   |
        |                                        |                          |         | 深交所：Y      | (total_turnover_t-1);首条记录取当前成交总额           |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | total_sell_order_volume                | 委托卖出总量             | <f8     | Y              | 是指直接到切片时间的还存在的, 所有委托卖单总量        |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | total_buy_order_volume                 | 委托买入总量             | <f8     | Y              | 是指直接到切片时间的还存在的，所有委托买单总量        |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | wt_avg_sell_price                      | 加权平均委卖价格         | <f8     | Y              | 单位：元                                              |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | wt_avg_buy_price                       | 加权平均委买价格         | <f8     | Y              | 单位：元                                              |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | prev_close                             | 昨收盘价                 | <f8     | Y              | 上一交易日的收盘价，上交所的收盘价格是最后一分钟的成  |
        |                                        |                          |         |                | 交均价                                                |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | open                                   | 开盘价                   | <f8     | Y              | 当日开盘价                                            |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | high                                   | 最高价                   | <f8     | Y              | 开盘至当前时刻所出现的最高成交价                      |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | low                                    | 最低价                   | <f8     | Y              | 开盘至当前时刻所出现的最低成交价                      |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | daily_close                            | 今日收盘价               | <f8     | Y              | 该交易日的收盘价，上交所的收盘价格是最后一分钟的成交均|
        |                                        |                          |         |                | 价（在最后一笔行情上更新，其余行值为0）               |                              
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | sell_level_no                          | 申卖价格档位数           | <f8     | Y              | 表示揭示的档位数，取值（0,10）                        |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | buy_level_no                           | 申买价格档位数           | <f8     | Y              | 表示揭示的档位数，取值（0,10）                        |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+

       
    bbla    
    
    .. code-block:: python3
    
        from simonsc.api import history_snapshot
        
        >>> dt = pd.Timestamp("2020-07-24 14:55:00")
        >>> fields=["datetime","last","buy_price_1","buy_volume_1","sell_price_1","sell_volume_1","sell_price_10"]
        >>> data = history_snapshot(order_book_id="600446.XSHG", dt=dt, bar_count=10, fields=fields)
        >>> print(data)
        
                                            last   buy_price_1   buy_volume_1   sell_price_1  sell_volume_1  sell_price_10
        order_book_id   datetime                                   
        600446.XSHG   2020-07-24 14:54:32   19.12     19.12         1100.         19.13,         1500.         19.26
                      2020-07-24 14:54:35   19.12     19.11         6600.         19.12,         57900.        19.25
                      2020-07-24 14:54:38   19.12     19.11         6800.         19.12,         57800.        19.25
                      2020-07-24 14:54:41   19.12     19.11        36400.         19.12,         57200.        19.25
                      2020-07-24 14:54:44   19.11     19.11        21200.         19.12,         55900.        19.25
                      2020-07-24 14:54:47   19.11     19.11         7400.         19.12,         52200.        19.25
                      2020-07-24 14:54:50   19.12     19.11         4700.         19.12,         40800.        19.25
                      2020-07-24 14:54:53   19.12     19.12        41800.         19.13,         9700.         19.26
                      2020-07-24 14:54:56   19.12     19.12        40900.         19.13,         9700.         19.26
                      2020-07-24 14:54:59   19.13     19.12        44000.         19.13,         9600.         19.26
    """

    dt = convert_datetime_to_str(dt)
   
    return SimonsClient.instance().history_snapshot(**locals())  



@assert_auth
@export_as_api
def history_transaction(
    order_book_id: str,
    tick_count: int,
    start_dt: datetime,
    end_dt: datetime,
    fields: List[str]=None,
    include_prehours: bool=False
) -> np.ndarray:
    """获取指定合约的历史快照数据
    
    :param order_book_id: 合约代码
    :param tick_count: 获取的逐笔成交条数, 与start_dt, end_dt, 三者必填两者
    :param start_dt: 获取数据的起始日期时间，e.g. “2017-01-12 09:33:05”
    :param end_dt: 获取数据的截止日期时间，e.g. “2017-01-12 09:33:05”
    :param fields: 返回数据字段。必填项。见下方列表。
    :param include_prehours: 是否包含盘前数据
    
    .. admonition:: 可支持的数据字段
        :class: dropdown, note
        
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | fields                                 | 中文名                   | dtype   | 是否是原始字段 |  注释                                                 |   
        +========================================+==========================+=========+================+=======================================================+
        | date                                   | 交易归属日期             | <i8     | Y              | yyyymmdd                                              |    
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | datetime                               | 交易发生时间             | <i8     | C              | yyyymmddhhmmssmmm，由交易日当天日期和数据生成时间        |
        |                                        |                          |         |                |（交易所直接下发的）合成。精确到10毫秒级               |       
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | trade_price                            | 成交价格                 | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | trade_volume                           | 成交数量                 | <f8     | Y              |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | trade_turnover                         | 成交金额                 | <f8     | 上交所：Y      | 成交价格 X 成交量                                     |
        |                                        |                          |         | 深交所：N      |                                                       |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+
        | buy_sell_flag                          | 内外盘标志               | O       | 上交所：Y      | 上交所：（深交所全部为NULL）                          |
        |                                        |                          |         | 深交所：N      | - 2013-04-15前，没有下发该字段，值为NULL；            |
        |                                        |                          |         |                | - 2013-04-15至今，下发了该字段，字段值含义分别如下：  |
        |                                        |                          |         |                |   B:外盘，主动买；S:内盘，主动卖；N:未知              |
        +----------------------------------------+--------------------------+---------+----------------+-------------------------------------------------------+

       
    bbla    
    
    .. code-block:: python3
    
        from simons.api import history_transaction
        
        >>> dt = pd.Timestamp("2020-07-24 14:55:00")
        >>> fields=["datetime","trade_price","trade_volume","trade_turnover"]
        >>> data = history_transaction(order_book_id="600446.XSHG", start_dt=dt, bar_count=10, fields=fields)
        >>> print(data)
        
    """
@assert_auth
@export_as_api
def get_factor_exposure(
    order_book_ids: List[str],
    bar_count: int,
    dt: datetime.datetime,
    fields: List[str]=None,
    frequency: str='1d',
) -> pd.DataFrame:
    """获取指定合约的历史因子数据，支持任意日频率xd(1d,5d)和分钟频率xm(1m,3m,5m,15m)的历史因子数据（当前只支持1d）。
    
    :param order_book_id: 合约代码
    :param bar_count: 获取的历史数据数量，必填项
    :param dt: 获取数据的截止日期时间，e.g. “2020-09-18”
    :param fields: 返回数据字段。必填项。见因子数据数据字典。
    :param frequency: 获取数据什么样的频率进行。'1d'或'1m'分别表示每日和每分钟，默认为1d
    
    Example1::
    
    获取中国平安和万科A(order_book_ids), 2020-09-18(dt)之前10(bar_count)天的return_mean_5和returns_skew_20(fields)因子数据
    
    ..  code-block:: python3
        
        import pandas as pd
        from simonsc.api import get_factor_exposure
    
        # 
        >>> dt = pd.Timestamp("2020-09-18")
        >>> fields=["datetime","return_mean_5","returns_skew_20"]
        >>> order_book_id_list = ["000001.XSHE","000002.XSHE"]
        >>> factor_exposure = get_factor_exposure(order_book_ids=order_book_id_list, dt=dt, bar_count=10, fields=fields, frequency="1d")
        >>> print(factor_exposure)
                                          return_mean_5  returns_skew_20
            order_book_id datetime                                  
            000001.XSHE   2020-09-07      -0.001771         0.585366
                          2020-09-08       0.003992         0.499581
                          2020-09-09      -0.001237         0.683064
                          2020-09-10       0.005955         0.571358
                          2020-09-11       0.000848         0.744097
                          2020-09-14       0.004979         0.487314
                          2020-09-15      -0.000927         0.436575
                          2020-09-16       0.003097         0.357694
                          2020-09-17       0.003072         0.572409
                          2020-09-18       0.013797         0.365532
            000002.XSHE   2020-09-07       0.008380        -0.107046
                          2020-09-08       0.007832        -0.028114
                          2020-09-09       0.003366        -0.196695
                          2020-09-10       0.004690        -0.285299
                          2020-09-11      -0.000413         0.327043
                          2020-09-14      -0.005120         0.512526
                          2020-09-15      -0.002978         0.489892
                          2020-09-16       0.001579         0.271366
                          2020-09-17      -0.002774         0.348217
                          2020-09-18       0.009297         1.139321
                          
    """
    dt = convert_datetime_to_str(dt)
   
    return SimonsClient.instance().get_factor_exposure(**locals())  
