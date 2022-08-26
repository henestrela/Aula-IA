import pandas as pd
import os

dirname = os.path.dirname(__file__)

datasetfull = pd.concat([pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2012.csv'),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2013.csv', low_memory=False),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2014.csv'),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2015.csv', low_memory=False),
          pd.read_csv(dirname +'/datas/reclamacoes-fundamentadas-sindec-2016.csv')])


print(datasetfull.columns)