from simonsc.object.csmar_table import csmar_class_dict
from simonsc import auth
from simonsc.utils import query
from simonsc.api import get_table_data


def get_csmar_table():
    for table in csmar_class_dict:
        data_query = query(csmar_class_dict[table]).limit(20)
        data = get_table_data(data_query)
        print(data)


def get_simons_csmar_table():
    from simonsc.api import get_current_financial_report_fast
    from simonsc.object.simons_csmar_table import simons_csmar_balance_sheet, simons_csmar_income, \
        simons_csmar_cash_flow
    from simonsc.api import all_instruments
    symbol_list = all_instruments(type="CS")["order_book_id"]
    sym_list = list(map(lambda x: x[:6], symbol_list))
    q_ = query(simons_csmar_balance_sheet).filter(simons_csmar_balance_sheet.SYMBOL.in_(sym_list))
    data = get_current_financial_report_fast(q_, "2018-07-13")
    print(data)
    q_ = query(simons_csmar_income).filter(simons_csmar_income.SYMBOL.in_(sym_list))
    data = get_current_financial_report_fast(q_, "2018-07-13")
    print(data)
    q_ = query(simons_csmar_cash_flow).filter(simons_csmar_cash_flow.SYMBOL.in_(sym_list))
    data = get_current_financial_report_fast(q_, "2018-07-13")
    print(data)
    # test3
    #


def get_simons_financial_data():

    from simonsc.object.simons_csmar_table import simons_csmar_balance_sheet
    from simons.api import get_financial_report_continuously
    auth("quantresearch", "quantresearch")
    q_ = query(simons_csmar_balance_sheet).filter(simons_csmar_balance_sheet.SYMBOL.in_(["000001", "000002", "000004"]))
    # --------------- get financial report pit history data -----------------
    data = get_financial_report_continuously(q_, "2020-12-25", 10)
    print(data)


if __name__ == '__main__':
    auth("quantresearch", "quantresearch")

    # get_csmar_table()
    # get_simons_csmar_table()
    get_simons_financial_data()
