from simonsc.object.csmar_table import csmar_tables, csmar_class_dict
from simonsc import auth
from simonsc.utils import query
from simonsc.api import get_table_data


if __name__ == '__main__':
    auth("quantresearch", "quantresearch")

    for table in csmar_class_dict:
        data_query = query(csmar_class_dict[table]).limit(20)
        data = get_table_data(data_query)
        print(get_table_data(data_query))
