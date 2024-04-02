import pandas as pd
import yfinance as yf
import numpy as np
#import matplotlib as mpl
from datetime import datetime
import datetime as dt
import streamlit as st

current_dateTime = datetime.now()
start = current_dateTime-dt.timedelta(days=7)


st.set_page_config(page_title="Scalping", page_icon="📈")

st.title("Scalping")

ticker=st.text_input('Ticker','PLTR,UPS')
ticker=ticker.split(",")

number = st.number_input("Insert a number of candles", value=4, placeholder="Type a number...")
periodos_atr = st.number_input("Insert a lenght for ATR", value=14, placeholder="Type a number...")

def Range(data,velas):
    data = data.tail(velas)
    maximo = data['High'].max()
    minimo = data['Low'].min()

    high_low = maximo-minimo 
    #high_low = data['High']/data['Low'].shift(60) -1
    return high_low


def ATR (data, periodos):
    high_low = data['High'] - data['Low']
    high_cp = np.abs(data['High'] - data['Close'].shift())
    low_cp = np.abs(data['Low'] - data['Close'].shift())    
    df = pd.concat([high_low, high_cp, low_cp], axis=1)
    true_range = np.max(df, axis=1)
    average_true_range = true_range.rolling(periodos).mean()
    return average_true_range

dicc_fin ={}

for i in ticker:
    data = yf.download(i,interval = '1m', start = start, end = current_dateTime)
    #print(data.tail(velas))
    res = Range(data,number)
    dicc_fin[i]=res

dcc_atr = {}
for x in ticker:
    data_atr = yf.download(x)
    atr=ATR(data_atr, periodos_atr)
    atr_last=atr.iloc[[-1]][0]
    dcc_atr[x]=atr_last

serie_Atr=pd.Series(dcc_atr)
df = pd.DataFrame(index= dicc_fin.keys(), columns= ['Rango'], data = dicc_fin.values())
df['ATR']=serie_Atr
df['Comparacion']= df['Rango']/df['ATR']

df = df.sort_values('Comparacion', ascending=False)

st.write(df)
