import pandas as pd
import matplotlib
import numpy as np
import csv

path_validation_list_csv = '/Users/match/Desktop/programming_test/python_test/pandas_test/_test_validation_list.csv'
path_parameter_csv = '/Users/match/Desktop/programming_test/python_test/pandas_test/_test_validation_parameters.csv'
pd_parameters = pd.read_csv(path_parameter_csv)

# print(pd_parameters)
#
#     bit  illumination    NR   filter   AE  mode
# 0  32.0         850.0   OFF  filter1  OFF  EE01
# 1  64.0         940.0  BODY  filter2   ON  EE02
# 2   NaN           NaN  CBLT  filter3  NaN  EE03
# 3   NaN           NaN   CES  filter4  NaN  EE04
# 4   NaN           NaN   NaN  filter5  NaN  EE06
# 5   NaN           NaN   NaN      NaN  NaN  FE01
# 6   NaN           NaN   NaN      NaN  NaN  FE02
# 7   NaN           NaN   NaN      NaN  NaN  FE03
# 8   NaN           NaN   NaN      NaN  NaN  FE04
# 9   NaN           NaN   NaN      NaN  NaN  FE06


def get_dict_from_csv_parameter(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        for row in reader:
            print(row)

# TODO: How to make dict like{'bit': [32, 64], 'illumination': [850, 940]}
# csv should be key, value, value, value, ...


def t_get_dict_from_csv_parameter(path):

    dict_param = {}
    with open(path, 'r') as f:
        content = f.read()
        lines = content.split('\n')
        for line in lines:
            print("line=", line)
            title = ""
            list_value = []
            columns = line.split(',')
            print(columns)
            for column in columns:
                if column != "":
                    list_value.append(column)
            title = list_value.pop(0)
            print(title)
            dict_param[title] = list_value
        return dict_param


dict_test = t_get_dict_from_csv_parameter(path_parameter_csv)
print('dict_test=', dict_test)
get_dict_from_csv_parameter(path_validation_list_csv)