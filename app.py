import streamlit as st
import math

st.header("Calculadora")

radio=st.number_input("Radio de la circunferencia")
st.write("El diámetro de la circunferencia es",radio*2*math.pi)
st.write("El área de la circunferencia es",math.pi*radio*radio)
st.write("El volumen de la esfera es",4*math.pi*pow(radio,3)/3
