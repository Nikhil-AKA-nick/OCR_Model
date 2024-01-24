import tensorflow as tf
from tensorflow import keras
import os

# Define a simple sequential model
def create_model():
    import tensorflow as tf

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu', input_shape=(32, 512, 1)),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(46, activation='softmax')
    ])
    

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

    return model

checkpoint_path = "DevModel\C3\model.ckpt-190169"
checkpoint_dir = os.path.dirname(checkpoint_path)


# Create a new model instance
model = create_model()

# Loads the weights
model.load_weights(checkpoint_path)

# print(model.summary())


