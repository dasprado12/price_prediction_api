import datetime 
from datetime import date
from dateutil.parser import parse
import pandas as pd
import numpy as np
import yfinance as yf
from pymongo import MongoClient  
import json


class UpdateDataFrame:

    def __init__(self, data_name):
        self.data_name = data_name

    def DateCheck(self):
        # Puxar os dados do mongo: -TODO

        client = MongoClient("mongodb+srv://pedro:pedro@cluster0.xyz6q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client.SMP
        collection = db[self.data_name]
        df = pd.DataFrame(list(collection.find()))
        #  -----------------------------

        # Puxar dados Locais
        # df = pd.read_csv('./price_prediction/Data/{}.csv'.format(self.data_name))

        # Pega o dia de hoje
        today_str = date.today().strftime("%Y-%m-%d")
        # Pega o ultimo dia do dataframe
        df_last_day = df["Date"].iloc[-1]

        # Confere se a base de dados está atualizada
        if df_last_day == today_str:
            return df
        else:
            num_days = np.busday_count(df_last_day, today_str)
            return self.DateUpdate(df, num_days, collection)
        

    def DateUpdate(self, df, days, collection):
        print(days)
        # Faz uma chamada na api para pegar os dias que faltam -TODO

        #PBR - Petrobras 
        #CIOXY - CIELO
        #ABEV - AMBEV
        #ITUB - ITAU

        stock_code = ''
        if self.data_name == 'AMBEV':
            stock_code = 'ABEV'
        elif self.data_name == 'CIELO':
            stock_code = 'CIOXY'
        elif self.data_name == 'ITAU':
            stock_code = 'ITUB'
        elif self.data_name == 'PETR4':
            stock_code = 'PBR'
        else:
            print("sem correspondencia para: " + self.data_name)

        stock_asset = yf.Ticker(stock_code)
        new_stock_prices=stock_asset.history(period="{}d".format(days))
        new_stock_prices = new_stock_prices.reset_index()
        # print(new_stock_prices)

        for i in range(len(new_stock_prices)):
            new_stock_prices['Date'].iloc[i] = new_stock_prices['Date'].iloc[i].strftime("%Y-%m-%d")


        df = df.append(new_stock_prices)
        df = df.reset_index()
        df.drop('index', inplace=True, axis=1)

        # atualiza os dados do mongo
        mydf = df.tail(len(new_stock_prices))
        print(mydf)


        x= collection.insert_many(mylist)
        print(x)
        # print(df[['Date', 'Close']].tail(10))
        # print(df.tail(10))


        # js= json.loads(reset.to_json(orient='records', date_format='iso'))

        # for date in js:
        #     date['Date']=date['Date'].split('T00:00:00.000Z')[0]

        # collection.insert_many(js)

        # Retorna a base de dados atualizada 
        return df

    
