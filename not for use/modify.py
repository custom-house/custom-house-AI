import pandas as pd
import numpy as np

brief = pd.read_csv('Data/brief.csv')
brief = brief.drop(['Unnamed: 0'], axis=1)

grouped_brief = brief.groupby(['routine_id'])

df_dum = pd.get_dummies(brief, columns=['appliance_id'])
df_dum = df_dum.drop(['appliance_name', 'user_id'], axis=1)

list = list(df_dum)[1:]

df_list = pd.DataFrame({'appliance_id_1': [], 'appliance_id_2': [], 'appliance_id_3': [], 'appliance_id_4': [],
                        'appliance_id_5': [], 'appliance_id_6': [], 'appliance_id_7': [], 'appliance_id_8': [],
                        'appliance_id_9': [], 'user_ID': []})

for idx in df_dum['routine_id'].unique():
    temp_list = df_dum[df_dum['routine_id'] == idx].drop('routine_id', axis=1)
    for item in list:
        df_list.at[idx, item] = temp_list[item].sum()

df_list = df_list.apply(np.int64)

df_list['user_ID'] = brief['user_id']

df_list.to_csv('Data/Routine_list.csv')
