
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
