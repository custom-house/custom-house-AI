import pandas as pd

routine = pd.read_csv('Data/Routine.csv')

appliance = routine['Appliance'].values

strings = []
routines = pd.DataFrame({'Appliance': []})

for idx in range(len(appliance)):
    strings.append(appliance[idx].rstrip(']}').lstrip('[{').split('},{'))
    for index in range(len(strings[0])):
        tempdf = pd.DataFrame(
            {'Appliance': strings[0][index]}, index=[idx])
        routines = pd.concat([routines, tempdf])
    strings = []

routines.reset_index(inplace=True)
routines = routines.rename(columns={'index': 'routine_ID'})

routines.to_csv('Data/appliances.csv')
