import pandas as pd
from pandas import DataFrame, Series
import csv
import numpy as np

ath_sera = "/Users/match/Desktop/programming_test/csv_test/Sera_Temperature_1981_2010.csv"
path_test_result = "/Users/match/Desktop/programming_test/csv_test/no_mode_result.csv"

df = pd.read_csv(path_test_result)
print("df=")
print(df)
#
#      no  mode result
# 0   1_1  1000     OK
# 1   1_1  1001     NG
# 2   1_1  1002     OK
# 3   1_1  1003     NG
# 4   1_2  1000     OK
# 5   1_2  1001     NG
# 6   1_2  1002     OK
# 7   1_2  1003     NG
# 8   1_3  1000     OK
# 9   1_3  1001     NG
# 10  1_3  1002     OK
# 11  1_3  1003     NG

"""
DataFrameの行を表示・抽出  (Line from DataFrame to List)
"""
print("----------DataFrameの行を表示・抽出  (Line from DataFrame to List)---------")

def to_ndarray_from_df(df):
    ndarray_df = df.values
    return ndarray_df


# DataDrame to ndarray
ndarray_df = to_ndarray_from_df(df)
print("ndarray=")
print(ndarray_df)

# ndarray=
# [['1_1' 1000 'OK']
#  ['1_1' 1001 'NG']
#  ['1_1' 1002 'OK']
#  ['1_1' 1003 'NG']
#  ['1_2' 1000 'OK']
#  ['1_2' 1001 'NG']
#  ['1_2' 1002 'OK']
#  ['1_2' 1003 'NG']
#  ['1_3' 1000 'OK']
#  ['1_3' 1001 'NG']
#  ['1_3' 1002 'OK']
#  ['1_3' 1003 'NG']]

# ndarray to list
list_line_df = ndarray_df.tolist()
print("list=")
print(list_line_df)
# list=
# [['1_1', 1000, 'OK'], ['1_1', 1001, 'NG'], ['1_1', 1002, 'OK'], ['1_1', 1003, 'NG'], ['1_2', 1000, 'OK'],
# ['1_2', 1001, 'NG'], ['1_2', 1002, 'OK'], ['1_2', 1003, 'NG'], ['1_3', 1000, 'OK'], ['1_3', 1001, 'NG'],
# ['1_3', 1002, 'OK'], ['1_3', 1003, 'NG']]


"""
DataFrameの列をlistに抽出  (Row from DataFrame to List)
"""
print("----------DataFrameの列をlistに抽出  (Row from DataFrame to List)---------")

def to_list_from_df_row(df, row_column):
    list_column = df[row_column].values.tolist()  # df -> ndarray -> list
    return list_column


list_row_column = to_list_from_df_row(df, 'no')
print("list_row_column=")
print(list_row_column)
# list_column=
# ['1_1', '1_1', '1_1', '1_1', '1_2', '1_2', '1_2', '1_2', '1_3', '1_3', '1_3', '1_3']

















