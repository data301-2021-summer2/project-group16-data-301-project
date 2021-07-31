import pandas as pd
import numpy as np

H21RawData=pd.read_csv("../../data/raw/world-happiness-report-2021.csv")
H19RawData=pd.read_csv('../../data/raw/2019.csv')
H18RawData=pd.read_csv('../../data/raw/2018.csv')
H17RawData=pd.read_csv('../../data/raw/2017.csv')
H16RawData=pd.read_csv('../../data/raw/2016.csv')
H15RawData=pd.read_csv('../../data/raw/2015.csv')
LivCostRawData=pd.read_csv('../../data/raw/cost_of_living 2020.csv')
GDPRawData=pd.read_csv('../../data/raw/gdp.csv')
H20RawData=pd.read_csv('../../data/raw/world-happiness-report.csv')


def load_process(path_to_csv):
# Method Chain 1
    df1=(
       pd.read_csv(path_to_csv)
       .drop(['Family','Freedom'],axis=1)
       .dropna(subset=['Happiness Score'])
    )
# Method Chain 2  
    df2=(
         df1
        .sort_values('Country')
        .rename(columns={'Country':'Country_Sorted'})
        .reset_index
      
    )
    
    return df2
    

def process_df(DataFrame):
    df=(DataFrame
          .drop(['Family','Freedom'],axis=1)
          .dropna(subset=['Happiness Score'])
          .reset_index(drop=True)
          .groupby('Region')['Happiness Rank']
          .max()
          .sort_values()
          .to_frame()
       )
    return df


def select_col (df):
    df=df[['Country','Happiness Rank','Happiness Score','Economy (GDP per Capita)','Freedom','Trust (Government Corruption)','Generosity']]
    return (df)



