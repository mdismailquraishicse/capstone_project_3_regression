import numpy as np
import pandas as pd

def outliers_capping(series):
    ''' This function takes a series as an input and returns a series after capping outliers '''
    q1 = series.quantile(.25)
    q3 = series.quantile(.75)
    iqr = q3-q1
    lower = q1 - (1.5*iqr)
    upper = q3 + (1.5*iqr)
    print('lower : ', lower)
    print('upper : ',upper)
    def treat(num):
        if num <= lower:
            return lower
        elif num >= upper:
            return upper
        else:
            return num
    return series.apply(treat)