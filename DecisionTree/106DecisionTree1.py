import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

data = pd.read_csv('Data/User_With_Unique_Routine_ID.csv')
data = data.drop(['Unnamed: 0', 'birth'], axis=1).apply(np.int64)

target = ['appliance_id_1', 'appliance_id_2', 'appliance_id_3', 'appliance_id_4', 'appliance_id_5', 'appliance_id_6', 'appliance_id_7','appliance_id_8', 'appliance_id_9', 'routine_id']
# drop =  ['household', 'id', 'age', 'sex_F', 'sex_M']
df_train, df_test = train_test_split(data, test_size=0.3,
                                     stratify = data['routine_id'],
                                     random_state=1)

clf = tree.DecisionTreeClassifier(random_state=1, max_depth=12)

train_x = df_train.drop(columns = target)
train_y = df_train['routine_id']
test_x = df_test.drop(columns = target)
test_y = df_test['routine_id']
print(train_x)
model = clf.fit(X = train_x, y = train_y)

plt.rcParams.update({'figure.figsize' : [12, 8],
                     'figure.dpi' : '100'})

tree.plot_tree(model,
               feature_names = train_x.columns,
               proportion = True,
               filled = True,
               rounded = True,
               impurity = False,
               label = 'root',
               fontsize = 10);

df_test['pred'] = model.predict(test_x)

conf_mat = confusion_matrix(y_true = df_test['routine_id'],
                            y_pred = df_test['pred'])

plt.rcParams.update(plt.rcParamsDefault)

p = ConfusionMatrixDisplay(confusion_matrix = conf_mat)

p.plot(cmap = 'Blues')
plt.show()

print(metrics.accuracy_score(y_true = df_test['routine_id'],
                            y_pred = df_test['pred']))
print(metrics.precision_score(y_true = df_test['routine_id'],
                            y_pred = df_test['pred'],
                            pos_label = 1))
print(metrics.recall_score(y_true = df_test['routine_id'],
                            y_pred = df_test['pred'],
                            pos_label = 1))
print(metrics.f1_score(y_true = df_test['routine_id'],
                            y_pred = df_test['pred'],
                            pos_label = 1))