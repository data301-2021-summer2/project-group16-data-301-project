import numpy as np
import pandas as pd
from functools import reduce
import seaborn as sns
from matplotlib import pyplot

def hap_load_and_process(url_or_path_to_csv_file, rename_dict,final_list):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .rename(columns=rename_dict)
          #.dropna()
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          #.assign(status=lambda x: np.where((x.period > 2014), 1, 0))
          .sort_values("country", ascending=True)
          .reset_index(drop=True)
          .loc[:, final_list]
      )

    # Make sure to return the latest dataframe

    return df2 

def ind_load_and_process(url_or_path_to_csv_file, ind):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .rename(columns={"Location":"country","Period":"period","Value":ind})
          #.dropna()
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(status=lambda x: np.where((x.period > 2014), 1, 0))
          .sort_values(['country','period'],ascending=[True, True], ignore_index=True)
          .reset_index(drop=True)
          .loc[:, ["country", "period", ind,'status']]
      )

    # Make sure to return the latest dataframe

    return df2 

def merge_hap(data_frames):
    
    merged= reduce(lambda  left,right: pd.merge(left,right,on=['country'],
                                            how='inner'), data_frames)
    return merged
    
def filter_years(df):
    #df['status'] = df.apply(keep_or_discard,axis='columns')
    df=df.loc[df['status'] == 1]
    df=df.drop(columns=['status'])
    return df

def edit_data(dataFrame):
    
    numbs=list(dataFrame[list(dataFrame.columns)[2]])
    for string in numbs:
        loc = string.find(' ')
        numbs[numbs.index(string)]=string[0:loc].replace(',','')

    return numbs

def clean_ind(df):
    
    df=filter_years(df)
    df[[list(df.columns)[2]]]=edit_data(df)
    
    return df


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



