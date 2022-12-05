import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Data/User_With_Unique_Routine_ID.csv")


data['age'] = round((20230000-data['birth'])/10000)

x = data[['age', 'household', 'sex_F', 'appliance_id_1', 'appliance_id_2', 'appliance_id_3', 'appliance_id_4', 'appliance_id_5', 'appliance_id_6', 'appliance_id_7', 'appliance_id_8', 'appliance_id_9']]


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4).fit(data)
x['cluster'] = kmeans.labels_

sns.lmplot('household', 'appliance_id_1', data=data, fit_reg=False, hue='cluster')

sns.lmplot('age', 'appliance_id_1', data=data, fit_reg=False, hue='cluster')

sns.lmplot('sex_F', 'appliance_id_1', data=data, fit_reg=False, hue='cluster')

