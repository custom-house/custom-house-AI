import pandas as pd
import random

user = pd.read_csv('User.csv')
routine = pd.read_csv('Routine.csv')

for idx in range(len(user)):
    for _ in range(3):
        index = random.randint(0, len(routine))
        print(index)
