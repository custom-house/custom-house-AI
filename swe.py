import pandas as pd
import numpy as np

routine = pd.read_csv('Routine.csv')
# routine = routine.drop(['_id', 'command', 'timer', 'routine_name'], axis = 1)

# header_list = routine.columns.tolist()

appliance = routine['Appliance']
x = appliance.values
appliances = []

for idx in range(len(x)):
    appliances.append(x[idx].rstrip(']}').lstrip('[{').split('},{'))

for idx in range(len(appliances)):
    for index in range(len(appliances[idx])):
        print(appliances[idx][index])
    print()
