import numpy as np
import pandas as pd

def showSCDMU(df):
    '''
    Input : df,
    Print : shape, columns, number of duplicate, missing/nan count, unique count
    '''
    print(f" Rows and columns count for rossmann_df : {df.shape}")
    print()
    print('columns : ', list(df.columns))
    print()
    print(f"duplicates counts : {df.duplicated().sum()}")
    print()
    print('Nan\missing count :')
    print(df.isna().sum())
    print()
    print('Unique Count :')
    print(df.nunique())

def getMeanMedian(df, col, val):
    '''
    Input : df, col, val
    Output : df with mean and median
    '''
    return pd.concat([df[df[col]==val].describe().iloc[1], df[df[col]==val].describe().iloc[5]], axis=1)