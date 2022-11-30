import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm

routine = pd.read_csv('Data/Routine_With_User_ID.csv')
routine = routine.drop('Unnamed: 0', axis=1)

for idx in range(len(routine)):
    for i in range(len(routine.loc[idx, 'user_ID'].split(' '))):
        routine.loc[idx, 'user_' + str(i+1)] = routine.loc[idx,
                                                           'user_ID'].split(' ')[i]
routine = routine.fillna(0)

routine = routine.drop('user_ID', axis=1)

routine.to_csv('Data/Available_Data.csv')

# def cos_sim(A, B):
#     return dot(A, B) / (norm(A) * norm(B))


# for idx in range(len(data)):
#     print(cos_sim(data.iloc[0], data.iloc[idx]))
