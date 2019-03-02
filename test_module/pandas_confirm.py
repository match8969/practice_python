import pandas as pd
import matplotlib

# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#
# # 乱数を生成
# x = np.random.rand(100)
# y = np.random.rand(100)
#
# # 散布図を描画
# plt.scatter(x, y)
# plt.show()


# df is pandas.DataFrame. You use read_csv() to make DataFrame from svc.
# read_table is for tab separated, not comma.
df_csv = pd.read_csv('/Users/match/Desktop/programming_test/python_test/pandas_test/test_validation_list.csv')

print(df_csv)

# It is OK to use read_csv() for txt in case the sep is ,.
names1880 \
    = pd.read_csv('/Users/match/Desktop/programming_test/python_test/pandas_test/yob1880.txt',
                  names=['name', 'sex', 'births'])

print(names1880)
# Command + /   to CommentOut
#
#            name sex  birth
# 0          Mary   F   7065
# 1          Anna   F   2604
# 2          Emma   F   2003
#
#


# print(names1880.groupby('sex').births.sum())
#
# sex
# F     90993
# M    110491
# Name: births, dtype: int64


years = range(1880, 2011)

pieces = []
columns = ['names', 'sex', 'births']

for year in years:
    path = '/Users/match/Desktop/programming_test/python_test/pandas_test/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)  # ignore_index is to ignore original line index when loading.
# print('names=\n')
# print(names)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

print("total_birth.tail()=")
print(total_births.tail())

total_births.plot(title='Total births by sex and year')
# plt.show is needed to show graph.
# plt.show()


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


# print(names)
# 'group' arg is not needed because the instance is group object, maybe.
names = names.groupby(['year', 'sex']).apply(add_prop)  # worked
print(names)
#
#              names sex  births  year      prop
# 0             Mary   F    7065  1880  0.077643
# 1             Anna   F    2604  1880  0.028618
# 2             Emma   F    2003  1880  0.022013
# 3        Elizabeth   F    1939  1880  0.021309

np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
print(top1000)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='names', aggfunc=sum)

print(total_births)

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]

subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")

# plt.show() # worked

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))

# plt.show()  # worked

df = boys[boys.year == 2010]

print(df)

prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()

print(prop_cumsum[:10])
print(prop_cumsum.searchsorted(0.5))

df = boys[boys.year == 1900]
in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
print(in1900.searchsorted(0.5)+1)


def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q)+1

# Comment Out -> Commnad + /
# Error# TODO
# diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# diversity = diversity.unstack('sex')
#
# print(diversity.head())
#
#
# diversity.plot(title='Number of popular names in top 50%')

plt.show()