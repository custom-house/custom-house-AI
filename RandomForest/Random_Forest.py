import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('Data/User_With_Unique_Routine_ID.csv')
data = data.drop(['Unnamed: 0', 'birth'], axis=1).apply(np.int64)

target = ['appliance_id_1', 'appliance_id_2', 'appliance_id_3', 'appliance_id_4', 'appliance_id_5', 'appliance_id_6', 'appliance_id_7','appliance_id_8', 'appliance_id_9', 'routine_id']

df_train, df_test = train_test_split(data, test_size=0.3,
                                     stratify = data['routine_id'],
                                     random_state=1)

rfc = RandomForestClassifier(n_estimators=500, max_depth=6)

train_x = df_train.drop(columns = target)
train_y = df_train['routine_id']
test_x = df_test.drop(columns = target)
test_y = df_test['routine_id']

model = rfc.fit(X = train_x, y = train_y)

pred_train = rfc.predict(train_x)
pred_test = rfc.predict(test_x)

df_test['pred'] = model.predict(test_x)
print(df_test[['routine_id', 'pred']])
conf_mat = confusion_matrix(y_true = df_test['routine_id'],
                            y_pred = df_test['pred'])

plt.rcParams.update(plt.rcParamsDefault)

p = ConfusionMatrixDisplay(confusion_matrix = conf_mat)

p.plot(cmap = 'Blues')
plt.show()

print(rfc.score(train_x, train_y))
print(rfc.score(test_x, test_y))