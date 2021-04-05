import streamlit as st
import SessionState
from utils import load_model, return_prediction


def main(model):

    st.title('Clasificador de animales')

    st.header("A continuación un clasificador de animales:")

    uploaded_file = st.file_uploader(label="Selecciona una imagen de un animal:",
                                     type=["png", "jpeg", "jpg"])

    session_state = SessionState.get(pred_button=False)

    if not uploaded_file:
        st.warning("Por favor subir una imagen.")
        st.stop()
    else:
        session_state.uploaded_image = uploaded_file.read()

        if st.checkbox('Mostrar imagen'):
            st.image(session_state.uploaded_image, use_column_width=True)

        if st.button('Identificar'):
            session_state.pred_button = True

        if session_state.pred_button:
            label, prob = return_prediction(session_state.uploaded_image, model, IMG_SHAPE)

            st.write(f"Su predicción es {prob:2.2f}% {label}")

            session_state.feedback = st.selectbox(
                "¿Es correcta la predicción?",
                ("Seleccione una opción", "Si", "No"))

            if session_state.feedback == "Seleccione una opción":
                pass
            elif session_state.feedback == "Si":
                st.write("Si desea puede ayudarnos identificando otras imágenes de animales.")
            else:
                st.write("Seguiremos trabajando en mejorar nuestras predicciones.")

            st.write("Muchas gracias por participar.")


if __name__ == '__main__':
    IMG_SHAPE = (224, 224)
    MODEL = load_model('model_efficienttetb0.h5')

    main(MODEL)
