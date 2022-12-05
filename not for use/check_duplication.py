import pandas as pd

routine = pd.read_csv('Data/Brief_Routine.csv')

# routine = routine.drop(['Unnamed: 0', 'user_ID'], axis=1)

result = routine.drop_duplicates().reset_index().drop('index', axis=1)

temp = pd.DataFrame(result.sum(axis=1))

idx = pd.DataFrame(temp[temp[0] == 1]).reset_index()

for i in range(len(idx)):
    print(idx.loc[i, 'index'])
    result.drop(idx.loc[i, 'index'], inplace=True)

result.to_csv('Data/Unique_Brief_Routine.csv')