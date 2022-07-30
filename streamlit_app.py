import streamlit as st
import pandas as pd
import time

st.title('Here is your Flipcard Game to learn Spanish')
st.text('We gathered 2000 most used Spanish words and create a game for you.')




my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

if my_bar.progress == 100:
     st.write('Loading Complate')
