import pandas as pd
from itertools import combinations

routine = pd.DataFrame({'appliance_1': [], 'appliance_2': [], 'appliance_3': [], 'appliance_4': [],
                        'appliance_5': [], 'appliance_6': [], 'appliance_7': [], 'appliance_8': [], 'appliance_9': []})

items = routine.columns.values
count = 0
for element in list(combinations(items, 1)):
    routine.loc[count, element] = 1
    count += 1
for element in list(combinations(items, 2)):
    routine.loc[count, element] = 1
    count += 1
for element in list(combinations(items, 3)):
    routine.loc[count, element] = 1
    count += 1
for element in list(combinations(items, 4)):
    routine.loc[count, element] = 1
    count += 1

routine.to_csv('Data/All_Of_Routine.csv')
