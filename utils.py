import tensorflow as tf
from translate import translate
import numpy as np


value_classes = {
    0: 'cane',
    1: 'cavallo',
    2: 'elefante',
    3: 'farfalla',
    4: 'gallina',
    5: 'gatto',
    6: 'mucca',
    7: 'pecora',
    8: 'ragno',
    9: 'scoiattolo'
}


def load_model(model_name):
    model = tf.keras.models.load_model(model_name)

    return model


def process_image(image, img_shape):
    img = tf.io.decode_image(image, channels=3)
    img = tf.image.resize(img, img_shape)
    img = tf.expand_dims(img, axis=0)

    return img


def return_prediction(image, model, img_shape):
    image = process_image(image, img_shape)
    result = model.predict(image)

    prediction = value_classes[np.argmax(result)]
    traduction = translate[prediction]
    prob = max(result[0]) * 100

    return traduction, prob
