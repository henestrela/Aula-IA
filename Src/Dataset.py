import pandas as pd
import os
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
st = PorterStemmer()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('punkt')

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


#Diminuindo palavras com Stemming


print("Diminuindo palavras com Stemmin:")
stem = st.stem(datasetFull['NomeFantasiaRFB'].str.lower().str.cat(sep=' '))
print(len(stem))

#pegando os dados da planilha em lower case
tokensNomeFantasia = word_tokenize(stem)

print("Total de tokens inicias:")
print(len(tokensNomeFantasia))

#remove stopwords

stopwords = stopwords.words('portuguese')

res = [i for i in tokensNomeFantasia if i not in stopwords]

print("Total de tokens inicias apos a limpeza do stopwords:")
print(len(res))

#remove stopwords
setTokensNomeFantasia = set(res)

print("Total de tokens inicias apos o set:")
print(len(setTokensNomeFantasia))


vectorizer = CountVectorizer() 

X = vectorizer.fit_transform(setTokensNomeFantasia)

#print(vectorizer.vocabulary_)

print("Total apos limpezas:")
print(len(vectorizer.vocabulary_))

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 100)



tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(setTokensNomeFantasia)
print(pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out()))

print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix))