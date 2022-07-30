import streamlit as st
import pandas as pd
import time

st.title('Here is your Flipcard Game to learn Spanish')
st.text('We gathered 2000 most used Spanish words and create a game for you.')




my_bar = st.progress(0)

'''
for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

if percent_complete == 99:
     st.write('Loading Complete')
'''
     
#st.button(label, key=None, help=None, on_click=None, disabled=False)


st.number_input('Please set your level', min_value=10, max_value=2000, step=10, format=None, key=None, help=None, on_change=None)
