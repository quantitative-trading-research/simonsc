#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

import six
import datetime
import pandas as pd
from functools import wraps
from pymysql.converters import conversions, escape_item, encoders

from simonsc.object.wind_table import *
from simonsc.object.csmar_table import *
from simonsc.object.simons_csmar_table import *
from sqlalchemy.sql import compiler
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects import mysql as mysql_dialetct
from sqlalchemy.orm.query import Query
from sqlalchemy import and_, between


def is_str(s):
    return isinstance(s, six.string_types)


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


class ParamsError(Exception):
    pass


class FundamentalUtil(object):

    def __init__(self):
        pass


quarter_time_dict = {
    "1": ["%s-01-01 00:00:00", "%s-03-31 00:00:00"],
    "2": ["%s-04-01 00:00:00", "%s-06-30 00:00:00"],
    "3": ["%s-07-01 00:00:00", "%s-09-30 00:00:00"],
    "4": ["%s-10-01 00:00:00", "%s-12-31 00:00:00"],
    "5": ["%s-01-01 00:00:00", "%s-06-30 00:00:00"],
    "6": ["%s-01-01 00:00:00", "%s-12-31 00:00:00"],
    "7": ["%s-01-01 00:00:00", "%s-09-30 00:00:00"],
}


def get_symbol_list(query_object):
    comp = get_sql_and_param(query_object)
    keys = comp.positiontup
    symbol_list = list()
    for key in keys:
        if "SYMBOL" in key:
            symbol_list.append(comp.params[key])
    return symbol_list


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
    all_tables = wind_tables + csmar_tables + simons_csmar_tables
    table_str = "|".join(all_tables)
    # r'Cash_Flow|Balance_Sheet|Income_Statement|Financial_Indicator'
    m = re.findall(table_str, sql)
    return list(set(m))


def get_table_class(tablename):
    for class_dict in [csmar_class_dict, wind_class_dict]:
        if tablename.lower() in class_dict:
            return class_dict[tablename.lower()]


def get_fundamentals_sql_from_query(query_object, date=None, statDate=None):

    assert isinstance(query_object, Query), \
        "query_object must be a sqlalchemy's Query object. But what passed in was: " + str(type(query_object))

    stat_date = statDate
    offset = query_object._offset
    query_object = query_object.offset(offset)
    sql = compile_query(query_object)
    return sql


def get_sql_and_param(query):
    dialect = mysql_dialetct.dialect()
    statement = query.statement
    comp = compiler.SQLCompiler(dialect, statement)
    comp.compile()
    return comp


def compile_query(query):
    comp = get_sql_and_param(query)
    comp_params = comp.params
    params = []
    for k in comp.positiontup:
        v = comp_params[k]
        if six.PY2 and isinstance(v, six.string_types) and not isinstance(v, six.text_type):
            v = v.decode("utf8")
        v = escape_item(v, conversions, encoders)
        params.append(v)
    return (comp.string % tuple(params))


def stat_date_process(stat_date):
    year = stat_date[:4]
    if "q" not in stat_date:
        start_date, end_date = quarter_time_dict["6"]
    else:
        start_date, end_date = quarter_time_dict[stat_date[-1]]
    start_date = start_date % year
    end_date = end_date % year
    return start_date[:10], end_date[:10]



def to_date(date):
    """
    >>> convert_date('2015-1-1')
    datetime.date(2015, 1, 1)
    >>> convert_date('2015-01-01 00:00:00')
    datetime.date(2015, 1, 1)
    >>> convert_date(datetime.datetime(2015, 1, 1))
    datetime.date(2015, 1, 1)
    >>> convert_date(datetime.date(2015, 1, 1))
    datetime.date(2015, 1, 1)
    """
    if is_str(date):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    elif date is None:
        return None
    raise ParamsError("type error")