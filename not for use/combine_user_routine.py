import pandas as pd
import numpy as np

routine = pd.read_csv('Data/Available_Data.csv')
user = pd.read_csv('Data/User.csv')

routine = routine.drop('Unnamed: 0.1', axis=1).drop('Unnamed: 0', axis=1)
routine = routine.apply(np.int64)

user = user.drop(['name', 'password', 'user_id'], axis=1)
user = pd.get_dummies(user, columns=['sex'])

routine1 = routine.drop(['user_2', 'user_3', 'user_4', 'user_5'], axis=1).rename(
    columns={'user_1': 'id'})
routine2 = routine.drop(['user_1', 'user_3', 'user_4', 'user_5'], axis=1).rename(
    columns={'user_2': 'id'})
routine3 = routine.drop(['user_2', 'user_1', 'user_4', 'user_5'], axis=1).rename(
    columns={'user_3': 'id'})
routine4 = routine.drop(['user_2', 'user_3', 'user_1', 'user_5'], axis=1).rename(
    columns={'user_4': 'id'})
routine5 = routine.drop(['user_2', 'user_3', 'user_4', 'user_1'], axis=1).rename(
    columns={'user_5': 'id'})

routines = [routine1, routine2, routine3, routine4, routine5]
new_list = []

for element in routines:
    new_list.append(pd.merge(user, element, on='id'))

new_list0 = pd.DataFrame(new_list[0])
new_list1 = pd.DataFrame(new_list[1])
new_list2 = pd.DataFrame(new_list[2])
new_list3 = pd.DataFrame(new_list[3])
new_list4 = pd.DataFrame(new_list[4])

new_df = pd.concat([new_list0, new_list1])
new_df2 = pd.concat([new_list2, new_list3])
new_df3 = pd.concat([new_df, new_list4])
new_df = pd.concat([new_df2, new_df3])

sort_new_df = new_df.sort_values(by='id')
sort_new_df = sort_new_df.reset_index().drop(['index'], axis=1)
print(sort_new_df)
print(sort_new_df['id'].nunique())
