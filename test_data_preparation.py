#test_data preparation
from data_prep import data_preparation
import pandas as pd

#THE MOST PART PF THAT WILL BE REPALCED

#path to where the data is saved just for test
path = 'C:/Users/wendr/ds enviroment/files/churn.csv'

received_data = pd.read_csv(path)
print('data:',received_data.shape)

received_data.drop('Exited',axis=1,inplace=True)
print('original data shape',received_data.shape)


new_data = data_preparation(received_data)

print('modified data shape',new_data.shape)