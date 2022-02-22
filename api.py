#the goal is to build a api to 

#IMPORTS
import pandas as pd
import pickle as pk
from flask import Flask, request

from data_prep import data_preparation


#load model
path = 'churn.csv'



model_loaded = pk.load(open('model.pkl','rb'))


#instanciate Flask
app = Flask(__name__)

#forma de acesso POST = enviar resultados
@app.route('/predict',methods=['POST'])
def predict():

    #collect data
    test_json = request.get_json()
    #se foi passado dados na requisição
    if test_json:
        #se tem uma linha ou mais
        if isinstance(test_json, dict): #unique value
            df_row = pd.DataFrame(test_json, index=[0])
            df_row = data_preparation(df_row)
        else:
            df_row = pd.DataFrame(test_json, columns= test_json[0].keys())
            df_row = data_preparation(df_row)
            
    #prediction
    pred = model_loaded.predict(df_row)
    
    #variabel with the probability of the output
    prob = model_loaded.predict_proba(df_row)
    
    #prediction 
    df_row['prediction'] = pred
    
    #dataset creation
    df_prob = pd.DataFrame(prob)
    
    #put the probability of the chrun in the dataset with the prediction
    df_row['churn probability'] = df_prob[1]
    
    
    
    return df_row.to_json(orient='records')
    
    
    
if __name__ == '__main__':
    #start Flask
    app.run(host='0.0.0.0' , port='5000')



























'''
######################################################################################
#import the fuction to clean the data
from data_prep import data_preparation

#THE MOST PART PF THAT WILL BE REPALCED

#path to where the data is saved just for test
path = 'C:/Users/wendr/ds enviroment/files/churn.csv'

received_data = pd.read_csv(path)

print(received_data.head())
print('**'*20)
test = data_preparation(received_data)

print(test.head())
#data preaparion
print('*'*20,'model test','*'*20)

#loading the pkl model
pkl_path = 'C:/Users/wendr/ds enviroment/Portfolio project/churn bank project/pkl_files/'

#---feito1
model_loaded = pk.load(open(pkl_path+'model.pkl','rb'))

pred = model_loaded.predict(test)

print('*'*30)
print(pred)'''