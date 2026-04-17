import streamlit as st
import pandas as pd

st.title('🤖 Machine learning')

st.info(' this is a app for machine learning model')
df = pd.read_csv('penguine_species.csv')
df
