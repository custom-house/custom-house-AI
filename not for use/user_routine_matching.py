import pandas as pd
import numpy as np
import random

user = pd.read_csv('Data/User.csv')
routine = pd.read_csv('Data/All_Of_Routine.csv')

arr = [x for x in range(0, len(routine) - 1)]

for idx in range(len(user)):
    routine_list = random.sample(arr, 5)
    routine_list.sort()
    user.at[idx, 'routine_ID'] = str(
        routine_list).replace('[', '').replace(']', '').replace(',', '')

for idx in range(len(user)):
    for i in range(len(user.loc[idx, 'routine_ID'].split(' '))):
        user.loc[idx, 'routine_' + str(i+1)] = user.loc[idx, 'routine_ID'].\
            split(' ')[i]

routine = routine.drop('Unnamed: 0', axis=1)
routine = routine.fillna(0)
routine = routine.apply(np.int64)
routine = routine.reset_index().rename(columns={'index': 'routine_id'})

user = user.drop('routine_ID', axis=1)

user = user.drop(['name', 'password', 'user_id'], axis=1)
user = pd.get_dummies(user, columns=['sex'])

user[['routine_1', 'routine_2', 'routine_3', 'routine_4', 'routine_5']] = user[[
    'routine_1', 'routine_2', 'routine_3', 'routine_4', 'routine_5']].apply(np.int64)

user1 = user.drop(['routine_2', 'routine_3', 'routine_4', 'routine_5'], axis=1).rename(
    columns={'routine_1': 'routine_id'})
user2 = user.drop(['routine_1', 'routine_3', 'routine_4', 'routine_5'], axis=1).rename(
    columns={'routine_2': 'routine_id'})
user3 = user.drop(['routine_2', 'routine_1', 'routine_4', 'routine_5'], axis=1).rename(
    columns={'routine_3': 'routine_id'})
user4 = user.drop(['routine_2', 'routine_3', 'routine_1', 'routine_5'], axis=1).rename(
    columns={'routine_4': 'routine_id'})
user5 = user.drop(['routine_2', 'routine_3', 'routine_4', 'routine_1'], axis=1).rename(
    columns={'routine_5': 'routine_id'})

users = [user1, user2, user3, user4, user5]
new_list = []
for element in users:
    new_list.append(pd.merge(element, routine, on='routine_id'))

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

sort_new_df.to_csv('Data/User_With_Rouitne_ID.csv')
