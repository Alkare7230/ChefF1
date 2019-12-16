#coding:utf-8

"""
Ceci est ma Zone d'importations

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn import linear_model #modèle linéaire
from sklearn.metrics import mean_squared_error, r2_score #métriques d'évaluation
import warnings
warnings.simplefilter("ignore")
import seaborn as sns; sns.set()
from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV
import seaborn as sns; sns.set()
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#to make the interactive maps
import folium
from folium.plugins import FastMarkerCluster
import geopandas as gpd
from branca.colormap import LinearColormap

#to make the plotly graphs
import plotly.graph_objs as go
import plotly.plotly as py
from plotly.offline import iplot, init_notebook_mode
import cufflinks
import csv

import scrapy as scp
import bs4

#________________________________ sea_________________________________________________________________________________________#

#Ceci est sont tout mes CSV !!#

circuits2 = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\circuits.csv", encoding='iso-8859-1')
results = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export\\resultatslFinal.csv", sep=',')
driver = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export\\pilotefinal.csv",  encoding='utf-8')
status = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export\\statufinal.csv",  encoding='iso-8859-1')
pitStp = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export\\controlfinal.csv",  encoding='iso-8859-1')
control = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export\\controlfinal.csv",  encoding='iso-8859-1')
driverstand = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\driverStandings.csv",  encoding='iso-8859-1')
race = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\race2.csv", encoding='utf-8', sep=',')
qualif = pd.read_csv("C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\qualifying.csv", encoding='iso-8859-1')




#___________________________________________________________________________________________________________________________#
#Ceci ce sera ma zone de nettoyage#

circuits.head()
results.tail()
season.head()
del circuits2["url"]
del circuits2["alt"]
del driver['url']
del results['Unnamed: 0']

driver.isna()
driver.dropna(how='all')
finalres= res['position'].astype('int')
res  = results.fillna(0)
driv = driver.fillna(0)
qual  = qualif.fillna(0)
#qualif.groupby('number').position.mean()## le prix moyen  des appartements des différents quatiers de paris

#df1 = pandas.DataFrame({'A': [3, 5], 'B': [1, 2]}, index = [0, 1])
#df2 = pandas.DataFrame({'A': [6, 7], 'B': [4, 9]}, index = [2, 3])
#pandas.concat([df1, df2])

df1 = circuits2.merge(driver, left_on=True, right_on=True, how='inner')
resv = pd.rename(columns = {'rank' : 'stage', 'position' : 'post', 'time' :'temps'}, left_on='how_all')
#__________________________________________________________________________________________________________________________#
#Zone DATAVIZ
#df['neighbourhood'].value_counts().plot.pie()#
#plt.figure(figsize=(30,20))
#sns.set(style="darkgrid")
#graph= sns.countplot(x="neighbourhood", data=df)
#plt.figure(figsize=(30,20))
#sns.set(style="darkgrid")
#graph= sns.countplot(x="neighbourhood", data=df)
# round(df.name.nunique()/len(df)*100,2)#
#sns.lineplot(x="price", y="signal",
             #hue="neighbourhood", style="event",
             #data=df)


plt.figure(figsize=(21, 14))
sns.set(style="darkgrid")
graph = sns.countplot(x="fastestLapTime", data=results)

cam = ['post'].plot.pie()
plt.show()

cam.savefig('number.png')

plt.figure(figsize=(1, 2))
sns.set(style="darkgrid")
graph = sns.countplot(x="positionOrder", y="forname", data=results, Pilote)

meanlaps = res.laps.mean()
valuelaps = res.laps.value_counts()
plt.bar(driver, height='driverRef',  witdth='position', color='red')
plt.show()

qualifme = qualif.groupby('number').position.mean()
res = results.groupby('fastestLapSpeed').statusId.mean()
Valeurs = results.fastestLapSpeed.value_counts()

#feq = paris[paris['accommodates']== n_p]
#feq = feq.groupby('neighbourhood')['adjusted_price'].mean().sort_values(ascending=True)
#feq.plot.barh(figsize=(10, 8), color='b', width=0.5)
#plt.title("Prix par jour par quartier", fontsize=20)
#plt.xlabel('Prix moyen (Euro)', fontsize=12)
#plt.ylabel("")
#plt.show()

dry = driver[driver['driverRef']==driver]
dry = dry.groupby('number')['position'].mean().sort_values(ascending=True)
dry.plt.barth(figsize=(10, 8), color='r', width=0.5)
plt.title("Le top 100 des meilleurs Pilote F1", fontsize=10)
plt.xlabel('Pilote', fontsize=5)
plt.ylabel('position', fontsize=5)
plt.show()




merge = pd.merge(circuits2, driver, columns = {'name', 'forname', 'surname', 'lat', 'lng' }, left_on='all')


#_____________________________________________________________________________________________________________#
#Ecriture des modification#

circuits2.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\circuits2.csv')
driv.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\driver2.csv')
control.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\control2.csv')
driverstand.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\drivstand2.csv')
pitStp.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\pitstop2.csv')
qual.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\qualif2.csv')
res.to_csv('C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export\\resultatslFinal.csv' , sep=',')
#______________________________________________________________________________________________________________#
#raceId,year,round,circuitId,name,date,time,url#
def convertisseur(chemin):
    # Exemple de chemin :    'C:\\Users\\user\\Desktop\\TIPE\\tableau\\Frequence1_bis.csv'
    # /!\ Bien mettre les double slash et les guillemets. /!\

    # Tableau sera une liste de listes [[t1, acc1], [t2,acc2] ,... , [tn,accn]]
    raceId= []
    year = []
    round = []
    name = []
    date  = []
    time = []
    url = []

    # ouverture et lecture du fichier csv
    f = open(chemin)
    csv_f = csv.reader(f)

    # row = ligne ==> ça met le tableur dans le tableau sous forme de liste de listes
    for row in csv_f:
        Tableau.append(row)

    f.close

    # on récupère les "sous listes" du Tableau
    n = len(Tableau)
    for i in range(n - 1):
        Temps.append(Tableau[i][0])
        Acc.append(Tableau[i][1])

    return (Temps, Acc)

#________________________________________________________________________________________________________________#
#tentative de création de carte avec folium

lats2019 = circuits2['lat'].tolist()
lons2019 = circuits2['lng'].tolist()
name2019 = circuits2['circuitRef'].tolist()
fast = results['fastestLapTime']


locations = list(zip(lats2019, lons2019, name2019))

map1 = folium.Map(location=[48.8534, 2.3488], zoom_start=11.5)
FastMarkerCluster(data=locations).add_to(map1)
map1.save('C:\\Users\\user\\Desktop\\program\\F1chef\\template\\circuitmap.html')
map1
