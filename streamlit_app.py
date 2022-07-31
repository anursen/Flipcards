import streamlit as st
import pandas as pd
import time


class FlipCard:

  def __init__(self,level=100):
    '''



    '''
    self.level = level
    self.score = 0
    import pandas as pd
    import numpy as np
    path = 'es-en-2000.csv' 
    # path = input('Lütfen Soru Bankasının yolunu giriniz!') 
    self.df = pd.read_csv(path)
    self.df['act-psv'] = [int(i) for i in np.linspace(1,1,2000)]
    #print(df)
    self.set_level()


  def set_level(self):

    self.level_df = self.df.iloc[:self.level,:]
    #print(self.level_df)

  def get_question(self):
    try:
      self.question_df = self.level_df[self.level_df['act-psv'] != 0].sample(n=1)
      #self.question_index = self.question_df.index
      return self.question_df.es.values[0]
    except ValueError:
      return 'False'



  def get_answer(self):
      return self.question_df.en.values[0]
  
  def set_status(self):
    self.level_df.at[self.question_df.index.values[0],'act-psv'] = 0
    self.set_score()
  
  def set_score(self):
    self.score = self.level_df[self.level_df['act-psv'] == 1]['act-psv'].count()





st.title('Here is your Flipcard Game to learn Spanish')
st.text('We gathered 2000 most used Spanish words and create a game for you.')

level = None
seconds = None

with st.form("my_form"):
    st.write("Please set the word number")
    slider_val = st.slider("Word Count",min_value=10, max_value=2000, value=100, step=10)
    slider_val = st.slider("Question time",min_value=1, max_value=10, value=5, step=1)
    #checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        level = slider_val
        seconds = slider_val

st.write("Outside the form")



while level and seconds != None:

    game = FlipCard(level = level)
    question = game.get_question()
    

    
    



'''
my_bar = st.progress(0)


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



