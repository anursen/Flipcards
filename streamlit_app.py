import streamlit as st
import pandas as pd
import time

st.title('Here is your Flipcard Game to learn Spanish')
st.text('We gathered 2000 most used Spanish words and create a game for you.')



key1 = None
key2 = None

with st.form("my_form"):
    st.write("Please set the word number")
    slider_val = st.slider("Word Count",min_value=10, max_value=2000, value=100, step=10)
    slider_val = st.slider("Question time",min_value=1, max_value=10, value=5, step=1)
    #checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        key1 = slider_val
        key2 = slider_val
        st.write(key1,key2)

st.write("Outside the form")



while key1 and key2 != None:
    st.write('Lets go')




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
   
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.table(df)



