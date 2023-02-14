import streamlit as st

st.header("Calculadora")

radio=st.number_input("Radio de la circunferencia")
st.write("El diámetro de la circunferencia es",radio*2*math.PI)
