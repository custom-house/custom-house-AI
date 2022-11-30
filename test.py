import pandas as pd
import numpy as np
from itertools import combinations

data = pd.read_csv('Data/User_With_Unique_Routine_ID.csv')
data = data.drop(['Unnamed: 0', 'birth', 'routine_id', 'id'], axis=1).apply(np.int64)

header = data.columns.tolist()
header = header[4:]

for element2 in list(combinations(header, 2)) :
    len1 = len(data[data[element2[0]] == 1])
    len2 = len(data[data[element2[1]] == 1])
    len3 = len(data[(data[element2[0]] == 1) & (data[element2[1]] == 1)])
    
    print(element2[0], len1)
    print(element2[1], len2)
    print(element2[0], element2[1], len3)
    print(round(len3/len1 * 100, 2), round(len3/len2 * 100, 2))