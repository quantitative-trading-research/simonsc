# -*- coding: utf-8 -*-
from simonsc.client import SimonsClient
from simonsc.utils import *


@assert_auth
@export_as_api
def get_table_data(query_object):
    sql = get_fundamentals_sql_from_query(query_object)
    return SimonsClient.instance().get_fundamental_from_sql(sql=sql)



from simonsc.object.table import class_dict
from simonsc import auth
from simonsc.utils import query
from simonsc.api import get_table_data


if __name__ == '__main__':
    auth("quantresearch", "quantresearch")

    for table in class_dict:
        data_query = query(class_dict[table]).limit(20)
        print(table)
        print(get_table_data(data_query))