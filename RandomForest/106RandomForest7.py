import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import sklearn.tree as tree
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('Data/User_With_Unique_Routine_ID.csv')
data = data.drop(['Unnamed: 0', 'birth', 'routine_id', 'id'], axis=1).apply(np.int64)

df_train, df_test = train_test_split(data, test_size=0.3,
                                     stratify = data['appliance_id_7'],
                                     random_state=1)

rfc = RandomForestClassifier(n_estimators=500, max_depth=10)

train_x = df_train.drop(columns = 'appliance_id_7')
train_y = df_train['appliance_id_7']

test_x = df_test.drop(columns = 'appliance_id_7')
test_y = df_test['appliance_id_7']

model = rfc.fit(X = train_x, y = train_y)

pred_train = rfc.predict(train_x)
pred_test = rfc.predict(test_x)

estimator = model.estimators_[3]

tree.plot_tree(estimator,
               feature_names = train_x.columns,
               class_names = ['0', '1'],
               proportion = True,
               filled = True,
               rounded = True,
               impurity = False,
               label = 'root',
               fontsize = 10);

df_test['pred'] = model.predict(test_x)

conf_mat = confusion_matrix(y_true = df_test['appliance_id_7'],
                            y_pred = df_test['pred'],
                            labels = [0, 1])

plt.rcParams.update(plt.rcParamsDefault)

p = ConfusionMatrixDisplay(confusion_matrix = conf_mat,
                           display_labels = ('0', '1'))

p.plot(cmap = 'Blues')
plt.show()

print(metrics.accuracy_score(y_true = df_test['appliance_id_7'],
                            y_pred = df_test['pred']))
print(metrics.precision_score(y_true = df_test['appliance_id_7'],
                            y_pred = df_test['pred'],
                            pos_label = 1))
print(metrics.recall_score(y_true = df_test['appliance_id_7'],
                            y_pred = df_test['pred'],
                            pos_label = 1))
print(metrics.f1_score(y_true = df_test['appliance_id_7'],
                            y_pred = df_test['pred'],
                            pos_label = 1))