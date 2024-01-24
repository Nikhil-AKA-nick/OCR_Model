import tensorflow as tf
from tensorflow import keras

model_path = 'DevModel/1/'

# load saved model from pb file
Models = tf.saved_model.load(model_path)

