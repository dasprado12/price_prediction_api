from tensorflow.keras.models import model_from_json
from keras.preprocessing.sequence import TimeseriesGenerator
import pandas as pd

# gpus = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(gpus[0], True)

class LoadedModel:

    # -----------------------------------------------Load_model-------------------------------------------------------
    data_name = "PETR4_SA_1"
    look_back = 15
    epochs_num = 25

    json_file = open("./app/Models/{}/json/regressor-{}-{}.json".format(data_name, data_name, epochs_num), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("./app/Models/{}/h5/regressor-{}-{}.h5".format(data_name, data_name, epochs_num))

    # -----------------------------------------------Data-------------------------------------------------------------

    df = pd.read_csv('./app/Data/{}.csv'.format(data_name))

    close_data = df['Close'].values
    close_data = close_data.reshape((-1, 1))

    split_percent = 0.80
    split = int(split_percent * len(close_data))

    close_train = close_data[:split]
    close_test = close_data[split:]

    date_train = df['Date'][:split]
    date_test = df['Date'][split:]

    # train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20)
    # valid_data_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=1)
    test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)

    prediction = model.predict(test_generator)

    # close_train = close_train.reshape((-1))
    close_test = close_test.reshape((-1))
    prediction = prediction.reshape((-1))

