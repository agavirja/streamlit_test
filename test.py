import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# streamlit run D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\streamlit\test1\test.py
# https://streamlit.io/
# pipreqs --encoding utf-8 "D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\streamlit\test1"
# https://share.streamlit.io/
# cuenta de github - agavirja



# Data
# D:\Dropbox\Empresa\Buydepa\COLOMBIA\ADMINISTRATIVA\1-INMUEBLES\DATA_INMUEBLES_EN_VENTA.xlsx

st.title('hellow world')
st.text('Este es un texto que lo pongo')
st.markdown('## Esto es un markdown')

uploaded_file = st.file_uploader('Cargar archivos aca')

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())
    
    fig,ax = plt.subplots(1,1)
    ax.scatter(x=df['PRECIO DE VENTA'],y=df['ÁREA CONSTRUIDA'])
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    
    st.pyplot(fig)
    
    