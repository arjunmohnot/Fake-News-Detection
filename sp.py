import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("fakeNews.h5")
tflite_model = converter.convert()
open("fingers_latest.tflite", "wb").write(tflite_model)
