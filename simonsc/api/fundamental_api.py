# -*- coding: utf-8 -*-
from simonsc.client import SimonsClient
from simonsc.utils import *
from simonsc.api.datetime_api import get_previous_trading_date
FUNDAMENTAL_RESULT_LIMIT = 10000
from dateutil.relativedelta import relativedelta
import pdb
import time



@assert_auth
@export_as_api
def get_table_data(query_object):
    sql = get_fundamentals_sql_from_query(query_object)
    return SimonsClient.instance().get_fundamental_from_sql(sql=sql)


@assert_auth
@export_as_api
def get_table_data_by_sql(sql):
    return SimonsClient.instance().get_fundamental_from_sql(sql=sql)


def get_start_date(end_date, if_balance_sheet=False):
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    if if_balance_sheet:
        start = end + relativedelta(months=-3) + relativedelta(days=1)
    else:
        year = end.year
        start = datetime.date(year, 1, 1)
    return start


def get_report_pub_date(symbol_list, end_date):
    ann_dt_query = query(stk_fin_relforcdate).filter(stk_fin_relforcdate.ACCOUPERI == end_date,
                                                     stk_fin_relforcdate.SYMBOL.in_(symbol_list))
    data = get_table_data(ann_dt_query)
    data = data[["SYMBOL", "ACCOUPERI", "ACTRELDATE"]]
    data.rename(columns={"ACCOUPERI": "ENDDATE", "ACTRELDATE": "PUB_DATE"}, inplace=True)
    return data


def get_current_report_date(symbol_list, date, if_balance_sheet=True):
    """

    :param symbol_list:
    :param date:
    :param if_balance_sheet:
    :return:
    """
    if date is None:
        date = datetime.datetime.now() - datetime.timedelta(1)
    record_start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    record_start_date -= relativedelta(years=1)
    ann_dt_query = query(stk_fin_relforcdate).filter(stk_fin_relforcdate.ACTRELDATE.between(record_start_date, date),
                                                     stk_fin_relforcdate.SYMBOL.in_(symbol_list))
    data = get_table_data(ann_dt_query)
    data.sort_values("ACCOUPERI", ascending=True, inplace=True)
    data = data[["SYMBOL", "ACCOUPERI", "ACTRELDATE"]]
    data.rename(columns={"ACCOUPERI": "ENDDATE", "ACTRELDATE": "pub_date"}, inplace=True)
    current = data.groupby('SYMBOL').agg({'ENDDATE': 'max', "pub_date": "max"})
    # for income & cash_flow table
    # stk_fin_balance don't have attribute startdate
    current["STARTDATE"] = current["ENDDATE"].astype(str).apply(lambda x: get_start_date(x, if_balance_sheet))
    return current


@export_as_api
def get_current_financial_report(query_object, date):
    """
    get the latest financial report at the certain date
    :param query_object:
    :param date: string
    :return:
    """
    symbol_list = get_symbol_list(query_object)
    table_included = get_tables_from_sql(str(query_object.statement))

    current = get_current_report_date(symbol_list, date)
    begin_date, end_date = current["STARTDATE"].min(), current["ENDDATE"].max()
    begin_date, end_date = str(begin_date)[:10], str(end_date)[:10]
    del current["STARTDATE"]

    for table in table_included:
        if table == "stk_fin_balance":
            query_object = query_object.filter(csmar_class_dict[table].ENDDATE.between(begin_date, end_date))
        else:
            query_object = query_object.filter(csmar_class_dict[table].STARTDATE.between(begin_date, end_date),
                                               csmar_class_dict[table].ENDDATE.between(begin_date, end_date),
                                               csmar_class_dict[table].REPORTTYPEID < 5)

    first_table = table_included[0]
    for table in table_included[1:]:
        query_object = query_object.filter(csmar_class_dict[table].SYMBOL == csmar_class_dict[first_table].SYMBOL,
                                           csmar_class_dict[table].ENDDATE == csmar_class_dict[first_table].ENDDATE)
    res = get_table_data(query_object)
    res = res.T.reset_index().drop_duplicates().set_index("index").T
    res = pd.merge(res, current, on=["SYMBOL", "ENDDATE"])
    res.sort_values("SYMBOL", ascending=True, inplace=True)
    return res


def get_financial_report(query_object, stat_date):
    """
    :param query_object:
    :param stat_date: year+q+number, e.g "2015", "2015q1", "2016q3)
    :return:
    """
    # :param count: look back count number
    start_date, end_date = stat_date_process(stat_date)
    symbol_list = get_symbol_list(query_object)
    tables_strs = get_tables_from_sql(str(query_object.statement))
    tables = [get_table_class(x) for x in tables_strs]
    for table in tables:
        if table == stk_fin_balance:
            query_object = query_object.filter(table.ENDDATE == end_date)
        else:
            query_object = query_object.filter(table.STARTDATE == start_date, table.ENDDATE == end_date)

    for table in tables[1:]:
        query_object = query_object.filter(table.SYMBOL == tables[0].SYMBOL, table.ENDDATE == tables[0].ENDDATE)

    sql = compile_query(query_object)

    pos = sql.find("WHERE")
    if "SYMBOL" not in sql[:pos+1]:
        table_name = tables[0].__tablename__
        sql = sql.replace("SELECT ", "SELECT %s.SYMBOL, %s.ENDDATE, " % (table_name, table_name))

    date_df = get_report_pub_date(symbol_list, end_date)
    res = get_table_data_by_sql(sql)
    # remove duplicated columns
    res = res.T.reset_index().drop_duplicates().set_index("index").T
    res = pd.merge(res, date_df, on=["SYMBOL", "ENDDATE"])
    return res


@export_as_api
def get_financial_report_continuously(query_object, stat_date, count):
    """

    :param query_object:
    :param stat_date:
    :param count:
    :return:
    """
    table_included = get_tables_from_sql(str(query_object.statement))
    start_date = get_previous_trading_date(stat_date, count)
    start_date = str(start_date)[:10]
    first_table = table_included[0]
    for table in table_included:
        query_object = query_object.filter(simons_csmar_class_dict[table].date.between(start_date, stat_date))

    for table in table_included[1:]:
        query_object = query_object.filter(
            simons_csmar_class_dict[table].SYMBOL == simons_csmar_class_dict[first_table].SYMBOL,
            simons_csmar_class_dict[table].date == simons_csmar_class_dict[first_table].date)

    # start = time.time()
    res = get_table_data(query_object)
    # end = time.time()
    # print(end - start)
    return res


@export_as_api
def get_current_financial_report_fast(query_object, date):
    """
    get the latest financial report at the certain date
    :param query_object:
    :param date: string
    :return:
    """
    table_included = get_tables_from_sql(str(query_object.statement))

    first_table = table_included[0]
    for table in table_included:
        query_object = query_object.filter(simons_csmar_class_dict[table].date == date)

    for table in table_included[1:]:
        query_object = query_object.filter(simons_csmar_class_dict[table].SYMBOL == simons_csmar_class_dict[first_table].SYMBOL,
                                           simons_csmar_class_dict[table].date == simons_csmar_class_dict[first_table].date)

    res = get_table_data(query_object)
    return res


if __name__ == '__main__':
    from simonsc import auth
    auth("quantresearch", "quantresearch")
    q_ = query(simons_csmar_balance_sheet).filter(simons_csmar_balance_sheet.SYMBOL.in_(["000001", "000002", "000004"]))
    data = get_financial_report_continuously(q_, "2020-12-25", 10)
    data.to_csv("~/demo.csv")