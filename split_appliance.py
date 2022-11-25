import pandas as pd

appliances = pd.read_csv('appliances.csv')
appliances = appliances.drop('Unnamed: 0', axis=1)

detail = []
details = []
details_array = []
for idx in range(len(appliances)):
    detail.append(appliances['Appliance'][idx].split(','))
    for index in range(len(detail[idx])):
        details.append(detail[idx][index].split(':'))
    details_array.append(details)
    details = []

df_appliance = pd.DataFrame()

df_detail = pd.DataFrame({'appliance_id': [], 'appliance_name': [], 'power': [], 'set_ch': [], 'set_vol': [],
                          'briefing': [], 'anti_wrinkle': [], 'eco_dry': [], 'set_time': [], 'set_temp': [],
                          'fire_power': [], 'wind_power': [], 'set_mod': [], 'burner': [], 'preserve': [],
                          'reserve_time': [], 'spinning': [], 'rising': []})


for i in range(len(details_array)):
    for idx in range(len(details_array[i])):
        header = details_array[i][idx][0].strip('"')
        value = details_array[i][idx][1].strip('"')
        print(header, value)
        tempdf = pd.DataFrame({}, index=[idx])
    print()
