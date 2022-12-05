import pandas as pd
import numpy as np

routine = pd.read_csv('Data/Recommendation.csv')
routine = routine.rename(columns={'Unnamed: 0' : 'routine_ID'})

print(routine)

column_name = ['routine_ID', 'routine_name', 'command', 'timer', 'user_ID', 'Appliance']
df = pd.DataFrame()