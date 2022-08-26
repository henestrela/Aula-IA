import pandas as pd
import os

dirname = os.path.dirname(__file__)

if os.path.exists(dirname + '/Datas/reclamacoes-full.csv'):
  os.remove(dirname + '/Datas/reclamacoes-full.csv')


datasetFull = pd.concat([
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2012.csv'),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2013.csv', low_memory= False),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2014.csv'),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2015.csv', low_memory= False),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2016.csv')], ignore_index= True)


datasetFull.to_csv(dirname +'/Datas/reclamacoes-full.csv')


datasetFullAfterSave = pd.read_csv(dirname +'/datas/reclamacoes-full.csv',low_memory=False)



print('Shape:')
print(datasetFullAfterSave.shape)
print('\n\nColumns')
print(datasetFullAfterSave.columns)