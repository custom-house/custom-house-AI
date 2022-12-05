import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Data/User_ID_Routine.csv')
#assign generation variable by using age variable
data = data.assign(generation=(lambda x: x['age'] // 10))
dummy_data = pd.get_dummies(data['generation'])
data = pd.concat([data, dummy_data],axis=1)

data = data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'birth'], axis=1).apply(np.int64)

data.to_csv('Data/User_With_Generation.csv')

routine = pd.read_csv('Data/Unique_Brief_Routine.csv')

#heatmap
# corr = data.corr()
# plt.figure(figsize=(8, 8));
# sns.heatmap(corr,
#             vmax=0.8,
#             linewidths=0.01,
#             square=True,
#             annot=True,
#             cmap='YlGnBu');
# plt.show();

age_20 = data[data['generation'] == 2].iloc[:,3:8]
age_30 = data[data['generation'] == 3].iloc[:,3:8]
age_40 = data[data['generation'] == 4].iloc[:,3:8]
age_50 = data[data['generation'] == 5].iloc[:,3:8]

generations = [age_20, age_30, age_40, age_50]
counts = []

for element in generations :
    df = pd.DataFrame()
    for index in range(5) :
        df = pd.concat([df, element.iloc[:, index].value_counts().to_frame()], axis = 1)
    df = df.fillna(0).assign(count=lambda x :x.iloc[:,0] + x.iloc[:,1] + x.iloc[:,2] + x.iloc[:,3] + x.iloc[:,4])\
        .apply(np.int64).sort_values(by='count', ascending = False)
    counts.append(df['count'])

counts[0] = pd.DataFrame(counts[0])
counts[1] = pd.DataFrame(counts[1])
counts[2] = pd.DataFrame(counts[2])
counts[3] = pd.DataFrame(counts[3])

counts[0] = pd.concat([counts[0], routine], axis = 1)
counts[1] = pd.concat([counts[1], routine], axis = 1)
counts[2] = pd.concat([counts[2], routine], axis = 1)
counts[3] = pd.concat([counts[3], routine], axis = 1)

for element in counts :
    print(element)