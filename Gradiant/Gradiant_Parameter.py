import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('Data/User_With_Generation.csv')
data = data.drop(['Unnamed: 0', '2.0', '3.0', '4.0', '5.0', 'id', 'age'], axis = 1)

params = { 
    'n_estimators':[50,100,200],
    'max_depth' : [2,3,4,5],
    'learning_rate':[0.05,0.1,0.2]
         }

df_train, df_test = train_test_split(data, test_size=0.2,
                                     stratify = data['routine_1'],
                                     random_state=1)

train_x = df_train.drop(columns = 'routine_1')
train_y = df_train['routine_1']
test_x = df_test.drop(columns = 'routine_1')
test_y = df_test['routine_1']

gb_clf = GradientBoostingClassifier(random_state = 0)

model = gb_clf.fit(X = train_x, y = train_y)

grid_cv= GridSearchCV(gb_clf, param_grid= params , cv=2, verbose=1)
grid_cv.fit(train_x, train_y)

pred = grid_cv.best_estimator_.predict(test_x)
gb_accuracy = accuracy_score(test_y,pred)
print('GBM 정확도:{0:4f}'.format(gb_accuracy))

model = grid_cv.best_estimator_
pred = model.predict(test_x)
gb_accuracy = accuracy_score(test_y,pred)
print('GBM 정확도:{0:4f}'.format(gb_accuracy))