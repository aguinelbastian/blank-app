import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Testando configurações Streamlit")
st.button('Hit me')
st.text_input('Enter some text')

col1, col2 = st.columns(2)

col1.st.image('./haval_h6/carga_naocarregando.png')
col2.st.image('./haval_h6/porta_malas.png')
