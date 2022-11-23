import pandas as pd

routine = pd.read_csv('Routine.csv')
routine = routine.drop(['_id', 'command', 'timer', 'routine_name'], axis = 1)

# header_list = routine.columns.tolist()

print(routine)