import pandas as pd 
import numpy  as np 

# ingreso de los csv 

dfAmazon = pd.read_csv('C:/Users/FABIAN/Desktop/PI01-Data-Engineering/Datasets/amazon_prime_titles-score.csv')
dfDisney = pd.read_csv('C:/Users/FABIAN/Desktop/PI01-Data-Engineering/Datasets/disney_plus_titles-score.csv')
dfHulu = pd.read_csv('C:/Users/FABIAN/Desktop/PI01-Data-Engineering/Datasets/hulu_titles-score (2).csv')
dfNetflix = pd.read_csv('C:/Users/FABIAN/Desktop/PI01-Data-Engineering/Datasets/netflix_titles-score.csv')

# formato de fecha 

dfAmazon['date_added']= pd.to_datetime (dfAmazon['date_added'],errors='coerce')
dfDisney['date_added']= pd.to_datetime (dfDisney['date_added'],errors='coerce')
dfHulu['date_added']= pd.to_datetime (dfHulu['date_added'],errors='coerce')
dfNetflix['date_added']= pd.to_datetime (dfNetflix['date_added'],errors='coerce')

# cabio de NaN  por "g"
dfAmazon['rating'] = dfAmazon['rating'].fillna('G')
dfDisney['rating'] = dfDisney['rating'].fillna('G')
dfHulu['rating'] = dfHulu['rating'].fillna('G')
dfNetflix['rating'] = dfNetflix['rating'].fillna('G')

# cabio de  mayusculas a minusculas como todos  los df se cambian a tipo str tenemos que cambiar los valores de varias columnas 

dfAmazon = dfAmazon.astype(str).apply(lambda x: x.str.lower() if x.dtype == "object" else x)
dfAmazon  = dfAmazon.astype({ "release_year": int,"score":int})
dfAmazon['date_added']=pd.to_datetime(dfAmazon['date_added'])

dfDisney = dfDisney.astype(str).apply(lambda x: x.str.lower() if x.dtype == "object" else x)
dfDisney  = dfDisney.astype({ "release_year": int,"score":int})
dfDisney['date_added']=pd.to_datetime(dfDisney['date_added'])

dfHulu = dfHulu.astype(str).apply(lambda x: x.str.lower() if x.dtype == "object" else x)
dfHulu = dfHulu.astype({ "release_year": int,"score":int})
dfHulu['date_added']=pd.to_datetime(dfHulu['date_added'])

dfNetflix = dfNetflix.astype(str).apply(lambda x: x.str.lower() if x.dtype == "object" else x)
dfNetflix = dfNetflix.astype({ "release_year": int,"score":int})
dfNetflix['date_added']=pd.to_datetime(dfNetflix['date_added'])

# para poder separ los numero de las letas use el sguiente codigo pero no funciono 
#dfAmazon['duration_type'] =dfAmazon['show_id'].str.extract('s([\ d]+) ')