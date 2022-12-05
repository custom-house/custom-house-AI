import pandas as pd

json = pd.read_json('Data/user_data.json')
csv = pd.read_csv('Data/User.csv')

# json = json.reset_index().rename(columns ={'index' : 'id'})
# json = json.drop('id', axis = 1)
print(json)
json.to_csv('Data/user_data.csv')
