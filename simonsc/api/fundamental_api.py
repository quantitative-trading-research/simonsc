# -*- coding: utf-8 -*-

# from typing import List, Union
# import datetime
# import numpy as np
# import pandas as pd
from simonsc.client import SimonsClient
from simonsc.utils import *


# @assert_auth
# @export_as_api
# def all_instruments(type: str = None, date: Union[str, datetime.datetime, datetime.date] = None) -> pd.DataFrame:
#     """
#     获取simons目前支持的所有合约信息
#
#     :param type: 需要查询合约类型，例如：type='CS'代表股票。默认是所有类型
#     :param date: 查询时间点
#
#     其中type参数传入的合约类型和对应的解释如下
#
#
#     =========================   ====================================================
#     合约类型                     说明
#     =========================   ====================================================
#      CS                           Common Stock, 即股票
#      ETF                          Exchange Traded Fund, 即交易所交易基金
#      LOF                          Listed Open-Ended Fund，即上市型开放式基金
#      INDX                         Index, 即指数
#      Future                       Futures，即期货，包含股指、国债和商品期货
#     =========================   ====================================================
#     :example:
#
#     .. code-block:: python3
#
#         >>> instrument_df = all_instruments(type="CS")
#         >>> instrument_df.head()
#            order_book_id symbol industry_code exchange  status type listed_date
#         0   000001.XSHE   平安银行           J66     XSHE  Active   CS  1991-04-03
#         1   000002.XSHE    万科A           K70     XSHE  Active   CS  1991-01-29
#         2   000004.XSHE   国农科技           I65     XSHE  Active   CS  1991-01-14
#         3   000005.XSHE   世纪星源           N77     XSHE  Active   CS  1990-12-10
#         4   000006.XSHE   深振业A           K70     XSHE  Active   CS  1992-04-27
#     """
#     date = convert_datetime_to_str(date)
#     return SimonsClient.instance().all_instruments(**locals())


@assert_auth
@export_as_api
def get_table_data(query_object):
    sql = get_fundamentals_sql_from_query(query_object)
    return SimonsClient.instance().get_fundamental_from_sql(sql=sql)
