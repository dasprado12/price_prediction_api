import datetime 
from datetime import date
from dateutil.parser import parse
import pandas as pd
import numpy as np

class UpdateDataFrame:

    def __init__(self, data_name):
        self.data_name = data_name

    def DateCheck(self):
        # Puxar as datas do mongo
        # Fazer um daframe com elas
        # Checar a ultima data .tail(1)
        #   se a ultima data for a de hoje, retorna o dataframe
        #   se não for, passa para DateUpdate
        # Pega o dia de hoje
        today_str = date.today().strftime("%Y-%m-%d")
        df = pd.read_csv('./price_prediction/Data/{}.csv'.format(self.data_name))

        # Pega o ultimo dia do dataframe
        df_last_day = df["Date"].iloc[-1]
        # df_last_day = datetime.datetime.strptime(df_last_day, '%Y-%m-%d')

        if df_last_day == today_str:
            return df
        else:

            num_days = np.busday_count(df_last_day, today_str)
            return self.DateUpdate(df, num_days)
        

    def DateUpdate(self, df, days):
        print(days)
        # calcular o número de requisições a serem feitas
        # Faz as requisições em um loop for
        # Atualiza o datadrame
        # sobe para o mongo
        # Retorna o data Frame atualizado
        # print("Numero de dias: ", days)
        return df

    
