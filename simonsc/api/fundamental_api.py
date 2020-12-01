# -*- coding: utf-8 -*-
from simonsc.client import SimonsClient
from simonsc.utils import *


@assert_auth
@export_as_api
def get_table_data(query_object):
    sql = get_fundamentals_sql_from_query(query_object)
    return SimonsClient.instance().get_fundamental_from_sql(sql=sql)
