import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle
from termcolor import colored as cl

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2

def sagatavot_datus(datne, kolonna_x, kolonna_y):
    df = pd.read_csv(datne)
    X_var = df[kolonna_x].values
    Y_var = df[kolonna_y].values

    X_train, X_test, Y_train, Y_test = train_test_split(X_var, Y_var, test_size=0.2, random_state=0)
    return (X_train, X_test, Y_train, Y_test)

def parverst_kolonnu(df, kolonna):
    df[kolonna] = pd.to_numeric(df[kolonna])
    df[kolonna] = df[kolonna].astype('int64')
    return df

def modela_kvalitate(Y_test, results):
    print(cl('Dispersija:{}'.format(evs(Y_test, results)), 'red', attrs=['bold']))
    print(cl('Kvardrātiskā novirze:{}'.format(r2(Y_test, results)), 'red', attrs=['bold']))

def trenet_modeli(modelis, X_train, Y_train, X_test):
    modelis.fit(X_train, Y_train)
    result = modelis.predict(X_test)
    return modelis, result

def prognozejam_rezultatu(modelis, dati):
    rezultats = modelis.predict(dati)
    return rezultats

datne1 = "masinmacisanas/dati/auto_simple.csv"
kol_x1 = ["Volume", "Weight"]
kol_y1 = 'CO2'

X_train, X_test, Y_train, Y_test = sagatavot_datus(datne1, kol_x1, kol_y1)

modelis = LinearRegression()

modelis, rezultats = trenet_modeli(modelis, X_train, Y_train, X_test)

modela_kvalitate(Y_test, rezultats)