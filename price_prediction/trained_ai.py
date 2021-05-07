from tensorflow.keras.models import model_from_json
from keras.preprocessing.sequence import TimeseriesGenerator
import pandas as pd
import numpy as np
import json
import datetime
from .update import UpdateDataFrame


# gpus = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(gpus[0], True)

class LoadedModel:

    def SetParameters(self, data_name):
        # data_name = "PETR4_SA_1"
        # -----------------------------------------------Load_model-------------------------------------------------------
        json_file = open("./price_prediction/Models/{}/regressor-{}.json".format(data_name, data_name), 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("./price_prediction/Models/{}/regressor-{}.h5".format(data_name, data_name))
        return self.TrainModel(model, data_name)

    def TrainModel(self, model, data_name):
        look_back = 15
        # df = pd.read_csv('./price_prediction/Data/{}.csv'.format(data_name))
        # Create the dataframe
        getDataFrame = UpdateDataFrame(data_name)
        df = getDataFrame.DateCheck()

        print(df.head())

        close_data = df['Close'].values
        close_data = close_data[::-1]
        close_data = close_data[:1000]
        close_data = close_data.reshape((-1, 1))

        prototype_date = df['Date'].values
        prototype_date = prototype_date[::-1]
        prototype_date = prototype_date[:1000]

        # print("prototype_date")
        # print(prototype_date)
        # print(type(prototype_date))
        # print(len(prototype_date))


        close_test = close_data
        date_test = prototype_date[::-1]

        # train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20)
        # valid_data_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=1)
        test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)

        # price predictions
        test = model.predict(test_generator)

        # close_train = close_train.reshape((-1))
        # close_test = close_test.reshape((-1))
        # test = test.reshape((-1))
        
        prediction = model.predict(test_generator)

        close_test = close_test.reshape((-1))
        prediction = prediction.reshape((-1))
        # --------------------------------FORECASTING--------------------------------
        num_prediction = 30

        def predict(num_prediction, model, close_data, look_back):
            prediction_list = close_data[-look_back:]

            for _ in range(num_prediction):
                x = prediction_list[-look_back:]
                x = x.reshape((1, look_back, 1))
                out = model.predict(x)[0][0]
                prediction_list = np.append(prediction_list, out)
            prediction_list = prediction_list[look_back - 1:]

            return prediction_list

        def predict_dates(num_prediction, df):
            last_date = df['Date'].values[-1]
            prediction_dates = pd.date_range(last_date, periods=num_prediction + 1).tolist()
            return prediction_dates

        forecast = predict(num_prediction, model, close_data, look_back)
        forecast_dates = predict_dates(num_prediction, df)
        close_data = close_data.reshape((-1))

        foracast_dates_aux = []
        for f_date in forecast_dates:
            foracast_dates_aux.append(f_date.strftime('%Y-%m-%d'))

        forecast_dates = foracast_dates_aux
        del forecast_dates[0]

        counter = 0
        # array correction
        # make 'close_test' and 'prediciton' with the same length
        aux = []
        for i in range(look_back):
            aux.append(None)
            counter = counter +1

        prediction = np.concatenate((prediction, aux))

        # increassing the size of 'close_test' and 'prediciton' according to 'forecast'
        aux = []
        for i in range(forecast.size -1):
            aux.append(None)
        prediction = np.concatenate((prediction, aux))
        close_test = np.concatenate((close_test, aux))

        # increasing the size of 'forecast' and making it begging on the last elemente of close test
        aux = []
        for i in range(close_test.size - forecast.size):
            aux.append(None)
        forecast = np.concatenate(( aux, forecast))

        concatenated_date = np.concatenate((date_test, forecast_dates))

        # testes -----------------------------

        # print("close_test")
        # print(close_test[:10])
        # print(type(close_test))
        # print(len(close_test))

        # print("prediction")
        # print(prediction[:10])
        # print(type(prediction))
        # print(len(prediction))

        # print("forecast")
        # print(forecast[:10])
        # print(type(forecast))
        # print(len(forecast))

        # # # print("date_test")
        # # # print(date_test[-10:])
        # # # print(type(date_test))
        # # # print(len(date_test))

        # # # print("forecast_dates")
        # # # print(forecast_dates)
        # # # print(type(forecast_dates))
        # # # print(len(forecast_dates))

        # print("concatenated_date")
        # print(concatenated_date[-40:])
        # print(type(concatenated_date))
        # print(len(concatenated_date))

        # ------------------------------------

        return_object={
            "name": "PETR4",
            "values":{
                "real": close_test.tolist(),
                "tested": prediction.tolist(),
                "forecast": forecast.tolist(),
                # "date": json.dumps(concatenated_date.tolist()),
                "date": concatenated_date.tolist(),
                # "forecast_date": json.dumps(forecast_dates.tolist())
            }
        }

        return return_object

