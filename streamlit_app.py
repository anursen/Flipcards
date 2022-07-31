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


st.number_input('Please set your level(Max 2000)', min_value=10, max_value=2000, step=10, format=None, key=None, help=None, on_change=None)


col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")

with col2:
    st.header("A dog")


with col3:
    st.header("An owl")

for i in range(3):
     st.write(i)
   
df = pd.DataFrame({'es':'en','si':'yes'})
st.table(df)
