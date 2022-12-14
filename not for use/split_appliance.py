import pandas as pd
import numpy as np

appliances = pd.read_csv('Data/appliances.csv')
appliances = appliances.drop('Unnamed: 0', axis=1)
routine = pd.read_csv('Data/Routine_With_User_ID.csv')

detail = []
details = []
details_array = []
for idx in range(len(appliances)):
    detail.append(appliances['Appliance'][idx].split(','))
    for index in range(len(detail[idx])):
        details.append(detail[idx][index].split(':'))
    details_array.append(details)
    details = []

df_detail = pd.DataFrame({'appliance_id': [], 'appliance_name': [], 'power': [], 'set_ch': [], 'set_vol': [],
                          'briefing': [], 'anti_wrinkle': [], 'eco_dry': [], 'set_time': [], 'set_temp': [],
                          'fire_power': [], 'wind_power': [], 'set_mod': [], 'burner': [], 'preserve': [],
                          'reserve_time': [], 'spining': [], 'rinsing': [], 'routine_id': [], 'user_id': []})

for i in range(len(details_array)):
    for idx in range(len(details_array[i])):
        header = details_array[i][idx][0].strip('"')
        value = details_array[i][idx][1].strip('"')
        df_detail.at[i, header] = value
        df_detail.at[i, 'routine_id'] = appliances['routine_ID'][i]

df_detail['user_id'] = routine['user_ID']

df_detail['routine_id'] = df_detail['routine_id'].apply(np.int64)

df_brief = df_detail[['appliance_id',
                      'appliance_name', 'routine_id', 'user_id']]

df_detail.to_csv('Data/details.csv')
df_brief.to_csv('Data/brief.csv')
