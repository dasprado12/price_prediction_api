from .update import UpdateDataFrame


class UpdateDataFrame:

    def __init__(self):
        df = self.DateCheck(df)
        return df
        

    def DateCheck(self, df):
        # Puxar as datas do mongo
        # Fazer um daframe com elas
        # Checar a ultima data .tail(1)
        #   se a ultima data for a de hoje, retorna o dataframe
        #   se não for, passa para DateUpdate
        df = pd.read_csv('./price_prediction/Data/{}.csv'.format(data_name))
        if df.tail(1)[0] == DateTime.Today:
            return df
        else:
            return self.DateUpdate(df)
        

    def DateUpdate(self, df):
        # calcular o número de requisições a serem feitas
        # Faz as requisições em um loop for
        # Atualiza o datadrame
        # sobe para o mongo
        # Retorna o data Frame atualizado

        return df

    
dataFrame = UpdateDataFrame()
