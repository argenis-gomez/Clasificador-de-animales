import streamlit as st
from utils import process_image, load_model


def return_prediction(image, model):
    image = process_image(image, img_shape=IMG_SHAPE)
    prediction = model.predict(image)

    return prediction


def main(model):

    st.title('Claificador de animales')

    st.write("A continuación encontraremos un clasificador de animales:")

    uploaded_file = st.file_uploader(label="Selecciona una imagen de animales:",
                                     type=["png", "jpeg", "jpg"])

    if not uploaded_file:
        st.warning("Por favor subir una imagen.")
        st.stop()
    else:
        image = uploaded_file.read()
        st.image(image, use_column_width=True)
        button = st.button('Predicción')
        if button:
            prediction = return_prediction(image, model)

            if prediction[0][0] > .5:
                label = 'Perro'
                prob = prediction[0][0] * 100
            else:
                label = 'Gato'
                prob = (1 - prediction[0][0]) * 100

            st.write(f"Su predicción es {prob:2.2f}% {label}")


if __name__ == '__main__':
    IMG_SHAPE = (64, 64)
    MODEL = load_model('model_acc90.h5')

    main(MODEL)
