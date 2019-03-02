import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import csv

path_test_result = "/Users/match/Desktop/programming_test/csv_test/no_mode_result.csv"
path_output_csv = "/Users/match/Desktop/programming_test/csv_test/for_hoshino_san.csv"




def dict_k_col1_v_cols(list_param):
    dict_k_col1_v_cols = {}
    for lines in list_lines:
        if lines[0] not in dict_k_col1_v_cols.keys():
            dict_k_col1_v_cols[lines[0]] = []
        for v_cols in lines[1:]:
            dict_k_col1_v_cols[lines[0]].append(v_cols)

    return dict_k_col1_v_cols


def write_csv_for_hosiho_format(dict_param, csv_write_path):
    line_str = ""
    for k in dict_param.keys():
        line_str += k
        for v in dict_param[k]:
            line_str += ','
            line_str += str(v)
        line_str += '\n'

    with open(path_output_csv, 'w') as f:
        f.write(line_str)


df = pd.read_csv(path_test_result)
list_lines = df.values.tolist()

dict_k_col1_v_cols = dict_k_col1_v_cols(list_lines)
write_csv_for_hosiho_format(dict_k_col1_v_cols, path_output_csv)

print(dict_k_col1_v_cols)



