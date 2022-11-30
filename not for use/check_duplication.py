import pandas as pd
import numpy as np

routine = pd.read_csv('Data/Routine_list.csv')

routine = routine.drop(['Unnamed: 0', 'user_ID'], axis=1)

result = routine.drop_duplicates().reset_index().drop('index', axis=1)

result.to_csv('Data/Unique_Routine_List.csv')