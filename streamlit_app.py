import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Testando configurações Streamlit")
st.button('Hit me')
st.text_input('Enter some text')

col1, col2 = st.columns(2)

with col1:
   st.header("Sem Carga")
   st.image("./haval_h6/carga_naocarregando.png")

with col2:
   st.header("Porta Malas")
   st.image("./haval_h6/porta_malas.png")
