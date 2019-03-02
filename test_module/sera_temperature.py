import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

path_sera = "/Users/match/Desktop/programming_test/csv_test/Sera_Temperature_1981_2010.csv"
path_outwork = "/Users/match/Desktop/programming_test/csv_test/Non_scheduled_hour_work_July.csv"

print('test start')

df_sera = pd.read_csv(path_sera, index_col='day')

print(df_sera)

df_sera.plot(title="Sera Avg Temperature on July from 1981 to 2010")

# plt.show()

df_out_work = pd.read_csv(path_outwork, index_col='year')

print(df_out_work)
df_out_work.plot(title="Non-Scheduled-Worked-Hour on July ")

plt.show()

