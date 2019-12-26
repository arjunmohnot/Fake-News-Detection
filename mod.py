import time
import keras
from keras.models import load_model
from tensorflow.keras.models import model_from_json
import json
import pandas as pd

from keras import backend as K
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
#from keras.utils.np_utils import to_categorical

#from keras.layers import Embedding
#from keras.layers import Dense, Input, Flatten
#from keras.layers import Conv1D, MaxPooling1D, Embedding, Dropout
#from keras.models import Model


#VALIDATION_SPLIT = 0.2


#prediction = loaded_model.predict(p)


def runs(inputs):
    MAX_SEQUENCE_LENGTH = 1000
    MAX_NB_WORDS = 200000
    EMBEDDING_DIM = 100

    json_file = open('fakeNews.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("fakeNews.h5")
    print("Loaded model from disk")

    
    newsInput=inputs
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
    tokenizer.fit_on_texts([newsInput])
    sequences = tokenizer.texts_to_sequences([newsInput])
    word_index = tokenizer.word_index
    data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    prediction = loaded_model.predict(data)
    K.clear_session()
    print(prediction)
    print(list(prediction[0])[0],"\n\n\n")
    
    return list(prediction[0])[0]
