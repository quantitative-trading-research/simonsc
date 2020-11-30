#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

import six
import datetime
import pandas as pd
from functools import wraps
from pymysql.converters import conversions, escape_item, encoders

from simons.object.table import *
from sqlalchemy.sql import compiler
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects import mysql as mysql_dialetct
from sqlalchemy.orm.query import Query


def _get_session():
    session = scoped_session(sessionmaker())
    return session


session = _get_session()


def query(*args, **kwargs):
    return session.query(*args, **kwargs)


def export_as_api(func):
    mod = sys.modules[func.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(func.__name__)
    else:
        mod.__all__ = [func.__name__]
    return func


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


def get_tables_from_sql(sql):

    table_str = "|".join(all_tables)
    # r'Cash_Flow|Balance_Sheet|Income_Statement|Financial_Indicator'
    m = re.findall(table_str, sql)
    return list(set(m))


def get_table_class(tablename):
    return class_dict[tablename.upper()]


def get_fundamentals_sql_from_query(query_object, date=None, statDate=None):

    assert isinstance(query_object, Query), \
        "query_object must be a sqlalchemy's Query object. But what passed in was: " + str(type(query_object))

    stat_date = statDate

    offset = query_object._offset
    # query_object._offset = None
    # query_object._limit = None

    tablenames = get_tables_from_sql(str(query_object.statement))
    tables = [get_table_class(name) for name in tablenames]

    by_year = False
    # if date:
    #    date = CalendarService.get_previous_trade_date(date)
    only_year = bool({"bank_indicator_acc", "security_indicator_acc",
                      "insurance_indicator_acc"} & set(tablenames))

    # for table in tables:
    #     if date:
    #         query_object = query_object.filter(table.day == date)
    #     else:
    #         if hasattr(table, 'statDate'):
    #             query_object = query_object.filter(table.statDate == stat_date)
    #         else:
    #             # 估值表, 在非交易日没有数据
    #             # 所以如果传入的非交易日, 就需要取得前一个交易日
    #             assert table is StockValuation
    #             if trade_day_not_after_stat_date is None:
    #                 trade_day_not_after_stat_date = CalendarService.get_previous_trade_date(stat_date)
    #             query_object = query_object.filter(table.day == trade_day_not_after_stat_date)

    # 连表
    # for table in tables[1:]:
    #     query_object = query_object.filter(table.code == tables[0].code)
    # limit = 100
    # 恢复 offset, limit
    # limit = 100000
    query_object = query_object.offset(offset)
    # query_object._limit = 10000
    # query_object = query_object.limit(limit)
    # print(query_object)
    sql = compile_query(query_object)
    return sql


def compile_query(query):
    dialect = mysql_dialetct.dialect()
    statement = query.statement
    comp = compiler.SQLCompiler(dialect, statement)
    comp.compile()
    enc = dialect.encoding
    comp_params = comp.params
    params = []
    for k in comp.positiontup:
        v = comp_params[k]
        if six.PY2 and isinstance(v, six.string_types) and not isinstance(v, six.text_type):
            v = v.decode("utf8")
        v = escape_item(v, conversions, encoders)
        params.append(v)
    return (comp.string % tuple(params))

