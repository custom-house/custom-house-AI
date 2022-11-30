import pandas as pd
import numpy as np
import random
from random import choices

user = pd.read_csv('Data/User.csv')
routine = pd.read_csv('Data/Unique_Routine_List.csv')
routine = routine.drop('Unnamed: 0', axis=1)

routine_1 = pd.DataFrame(routine[routine['appliance_id_1'] == 1]) #TV
routine_2 = pd.DataFrame(routine[routine['appliance_id_2'] == 1]) #Electronic Range
routine_3 = pd.DataFrame(routine[routine['appliance_id_3'] == 1]) #Light Oven
routine_4 = pd.DataFrame(routine[routine['appliance_id_4'] == 1]) #Washing Machine
routine_5 = pd.DataFrame(routine[routine['appliance_id_5'] == 1]) #Dryer
routine_6 = pd.DataFrame(routine[routine['appliance_id_6'] == 1]) #Robot Cleaner
routine_7 = pd.DataFrame(routine[routine['appliance_id_7'] == 1]) #Air Conditioner
routine_8 = pd.DataFrame(routine[routine['appliance_id_8'] == 1]) #Air Cleaner
routine_9 = pd.DataFrame(routine[routine['appliance_id_9'] == 1]) #Styler
routines = [routine_1, routine_2, routine_3, routine_4, routine_5, routine_6, routine_7, routine_8, routine_9]

age_20 = [1] * 7 + [2] * 6 + [3] * 2 + [4] * 1 + [5] * 2 + [6] * 3 + [7] * 10 + [8] * 5 + [9] * 1
age_30 = [1] * 8 + [2] * 6 + [3] * 3 + [4] * 1 + [5] * 3 + [6] * 5 + [7] * 10 + [8] * 7 + [9] * 1
age_40 = [1] * 9 + [2] * 5 + [3] * 3 + [4] * 1 + [5] * 2 + [6] * 6 + [7] * 10 + [8] * 7 + [9] * 1
age_50 = [1] * 10 + [2] * 6 + [3] * 1 + [4] * 1 + [5] * 1 + [6] * 2 + [7] * 10 + [8] * 6 + [9] * 1
ages = [age_20, age_30, age_40, age_50]
household_1 = [1] * 7 + [2] * 6 + [3] * 1 + [4] * 10 + [5] * 1 + [6] * 2 + [7] * 10 + [8] * 4 + [9] * 1
household_2 = [1] * 8 + [2] * 6 + [3] * 2 + [4] * 10 + [5] * 2 + [6] * 4 + [7] * 10 + [8] * 5 + [9] * 1
household_3 = [1] * 8 + [2] * 6 + [3] * 3 + [4] * 10 + [5] * 3 + [6] * 6 + [7] * 10 + [8] * 6 + [9] * 2
households = [household_1, household_2, household_3]

# female['household'] = int(str(choices(household,k=1)).replace('[','').replace(']',''))

for idx in range(len(user)):
    age = 2022 - int(str(user.iloc[idx, 0])[:4])
    user.at[idx, 'age'] = age
    age = str(age)[1]
    household = user.iloc[idx, 1]
    if int(age) < 2 :
        age = '2'
    elif int(age) > 5 :
        age = '5'
    if household > 3 :
        household = '3'
    pick1 = int(str(choices(ages[int(age) - 2], k = 1)).replace('[','').replace(']',''))
    pick2 = int(str(choices(households[int(household) - 1], k = 1)).replace('[','').replace(']',''))
    temp = pd.concat([routines[pick1 - 1], routines[pick2 - 1]])
    temp = temp.reset_index()
    arr = list(temp['index'].drop_duplicates())
    routine_list = random.sample(arr, 5)
    routine_list.sort()
    user.at[idx, 'routine_ID'] = str(
        routine_list).replace('[', '').replace(']', '').replace(',', '')

for idx in range(len(user)):
    for i in range(len(user.loc[idx, 'routine_ID'].split(' '))):
        user.loc[idx, 'routine_' + str(i+1)] = user.loc[idx, 'routine_ID'].\
            split(' ')[i]

routine = routine.fillna(0)
routine = routine.apply(np.int64)
routine = routine.reset_index().rename(columns={'index': 'routine_id'})

user = user.drop(['routine_ID', 'name', 'password', 'user_id'], axis=1)

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

sort_new_df.to_csv('Data/User_With_Unique_Routine_ID.csv')
