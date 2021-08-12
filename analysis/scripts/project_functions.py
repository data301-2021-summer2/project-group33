#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt    
import seaborn as sns

def load_and_process(Table):
    #Import data
    data = pd.read_csv(Table)

    #Clean, Process, and Wrangle Data
    df = data[data.Year > 1799]\
              .drop(columns=['Date', 'Location', 'Name', 'Age', 'Injury', 'Time', 'Unnamed: 14'])\
              .dropna(subset=['Year','Country'])\
              .reset_index(drop=True)
    
    df['Fatal'] = df['Fatal (Y/N)'].map({'Y': 1, 'y': 1, 'UNKNOWN':0, 'N': 0, 'M': 0, '2017': 0})
    df['Fatal'] = df['Fatal'].astype('bool')
    df = df.drop(df.columns[[6]], axis=1)
    df = df.drop(df.columns[[6]], axis=1)

    return df