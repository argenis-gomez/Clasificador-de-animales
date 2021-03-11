import tensorflow as tf


def load_model(model_name):
    model = tf.keras.models.load_model(model_name)

    return model


def process_image(image, img_shape):
    img = tf.cast(tf.io.decode_image(image, channels=3), dtype=tf.float16)
    img = tf.image.resize(img, [img_shape[0], img_shape[1]])
    img = tf.expand_dims(img, axis=0)

    return img / 255.
