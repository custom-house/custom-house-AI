import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm

data = pd.read_csv('Routine_list.csv')
data = data.drop('Unnamed: 0', axis=1)

print(data)


def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))


for idx in range(len(data)):
    print(cos_sim(data.iloc[0], data.iloc[idx]))
