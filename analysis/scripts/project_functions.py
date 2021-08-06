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