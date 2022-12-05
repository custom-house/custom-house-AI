import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
import seaborn as sns
import random

data = pd.read_csv('Data/User_With_Generation.csv')
data = data.drop(['Unnamed: 0', '2.0', '3.0', '4.0', '5.0', 'id', 'age'], axis = 1)

#heatmap
# corr = data.corr()
# plt.figure(figsize=(8, 8));
# sns.heatmap(corr,
#             vmax=0.8,
#             linewidths=0.01,
#             square=True,
#             annot=True,
#             cmap='YlGnBu');
# plt.title('Feature Correlation');
recom_array = []
while len(recom_array) < 3 :
    seed = random.randint(1,10000)
    df_train, df_test = train_test_split(data, test_size=0.2,
                                        stratify = data['routine_1'],
                                        random_state=1)

    gb = GradientBoostingClassifier(learning_rate=0.05,
                                        max_depth=3,
                                        random_state=seed)

    train_x = df_train.drop(columns = 'routine_1')
    train_y = df_train['routine_1']
    test_x = df_test.drop(columns = 'routine_1')
    test_y = df_test['routine_1']

    model = gb.fit(X = train_x, y = train_y)
    
    pred_train = gb.predict(train_x)
    pred_test = gb.predict(test_x)

    df_test['pred'] = model.predict(test_x)

    conf_mat = confusion_matrix(y_true = df_test['routine_1'],
                                y_pred = df_test['pred'])

    plt.rcParams.update(plt.rcParamsDefault)

    p = ConfusionMatrixDisplay(confusion_matrix = conf_mat)

    p.plot(cmap = 'Blues')
    # plt.show()

    print(gb.score(train_x, train_y))
    print(gb.score(test_x, test_y))

    user_data = [3, 17, 21, 22, 23, 0, 1, 2]
    user_array = []
    for _ in range(8) :
        user_array.append(user_data)
    user_x = pd.DataFrame(user_array, columns = ['household', 'routine_2', 'routine_3', 'routine_4', 'routine_5', 'sex_F', 'sex_M', 'generation'])
    pred_result = gb.predict(user_x)
    user_x['pred'] = model.predict(user_x)

    routine = pd.read_csv('Data/Unique_Brief_Routine.csv')
    recom = pd.DataFrame(routine.drop(['Unnamed: 0'],axis=1).loc[user_x['pred'][0]])
    recom = recom.transpose()
    print(recom)
    if len(recom_array) == 0 :
        recom_array.append(recom)
    else : 
        for idx in range(len(recom_array)) :
            if recom_array[idx].index.to_list() == recom.index.to_list() :
                recom_array.remove(recom_array[idx])
                break;
        recom_array.append(recom)
    
recom_array[0] = pd.DataFrame(recom_array[0])
recom_array[1] = pd.DataFrame(recom_array[1])
recom_array[2] = pd.DataFrame(recom_array[2])

recommend = pd.concat([recom_array[0], recom_array[1]])
recommend = pd.concat([recommend, recom_array[2]])

print(recommend)