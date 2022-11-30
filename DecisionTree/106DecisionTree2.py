import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

data = pd.read_csv('Data/User_With_Unique_Routine_ID.csv')
data = data.drop(['Unnamed: 0', 'birth', 'routine_id', 'id'], axis=1).apply(np.int64)

print(data)

df_train, df_test = train_test_split(data, test_size=0.3,
                                     stratify = data['appliance_id_2'],
                                     random_state=1)

clf = tree.DecisionTreeClassifier(random_state=1,
                                  max_depth=5)

train_x = df_train.drop(columns = 'appliance_id_2')
train_y = df_train['appliance_id_2']

model = clf.fit(X = train_x, y = train_y)

plt.rcParams.update({'figure.figsize' : [12, 8],
                     'figure.dpi' : '100'})

tree.plot_tree(model,
               feature_names = train_x.columns,
               class_names = ['0', '1'],
               proportion = True,
               filled = True,
               rounded = True,
               impurity = False,
               label = 'root',
               fontsize = 10);

test_x = df_test.drop(columns = 'appliance_id_2')
test_y = df_test['appliance_id_2']

df_test['pred'] = model.predict(test_x)

conf_mat = confusion_matrix(y_true = df_test['appliance_id_2'],
                            y_pred = df_test['pred'],
                            labels = [0, 1])

plt.rcParams.update(plt.rcParamsDefault)

p = ConfusionMatrixDisplay(confusion_matrix = conf_mat,
                           display_labels = ('0', '1'))

p.plot(cmap = 'Blues')
plt.show()

print(metrics.accuracy_score(y_true = df_test['appliance_id_2'],
                            y_pred = df_test['pred']))
print(metrics.precision_score(y_true = df_test['appliance_id_2'],
                            y_pred = df_test['pred'],
                            pos_label = 1))
print(metrics.recall_score(y_true = df_test['appliance_id_2'],
                            y_pred = df_test['pred'],
                            pos_label = 1))
print(metrics.f1_score(y_true = df_test['appliance_id_2'],
                            y_pred = df_test['pred'],
                            pos_label = 1))