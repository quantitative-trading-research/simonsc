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
