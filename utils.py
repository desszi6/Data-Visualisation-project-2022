#%%
"""
Imports
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import math
warnings.filterwarnings('ignore')
from pathlib import Path


def convert_currency(value):
    floatvalue = 0
    strvalue=""
    if type(value) == float:
        floatvalue = str('Unknown')
    elif "K" in value:
        strvalue=value.replace("K","").replace("€","")
        floatvalue=float(float(strvalue))
    elif "M" in value:
        strvalue=value.replace("M","").replace("€","")
        floatvalue=float(float(strvalue)*1000)
    else:
        floatvalue=value.replace("€","")
    return floatvalue

def convert_bodytype(value):
    rvalue = ""
    if type(value) == float:
        rvalue = str("Unknown")
    elif "Lean" in value:
        rvalue = str("Lean")
    elif "Normal" in value:
        rvalue = str("Normal")
    elif "Stocky" in value:
        rvalue = str("Stocky")
    else:
        rvalue = str("Unique")
    return rvalue
    
def weight_converter(value):
    if "kg" in value:
        rvalue = int(value[:-2])
    else:
        rvalue = int(int(value[:-3])*0.4535)
    return rvalue

def height_converter(value):
    if "'" in value:
        rvalue = value.split('\'')
        rvalue = round(int(value[0])*30.48+int(value[2:])*2.54,0)
    if "cm" in value:
        rvalue = value[:-2]
    return rvalue

def preproces_data(data):
    data['Value'] = data['Value'].apply(convert_currency).astype(int)
    data['Wage']  = data['Wage'].apply(convert_currency).astype(int)
    data['Release Clause'] = data['Release Clause'].apply(convert_currency)
    data['Name'] = data['Name'].replace('\d+', '', regex=True).str.lstrip()
    data['Position'] = data['Position'].astype(str).str[-3:].str.replace(">","")
    data['Loaned From'] = data['Loaned From'].str.split('">').str[1].str.replace("</a>","")
    data['Body Type'] = data['Body Type'].apply(convert_bodytype)
    data['Club Logo'] = data['Club Logo'].replace(r'/light_', r'', regex=True)
    data['Height'] = data['Height'].apply(height_converter)
    data['Weight'] = data['Weight'].apply(weight_converter)
 

    data['Club'] = data['Club'].fillna('None')
    data['Work Rate'] = data['Work Rate'].str.replace('N/A/ N/A','Unknown/Unknown')
    data['Real Face'] = data['Real Face'].fillna('No')
    data = data.fillna('Unknown')
    data = data.rename(columns={'Height':'Height(cm)','Weight':'Weight(kg)','Flag':'National Flag',
     'Value': 'Value(1,000€)', 'Wage': 'Wage(1,000€)', 'Work Rate': 'Offense/Defense intensity', 
     'Joined': 'Joined club (date, year)', 'Loaned from': 'Loaned from club'})
    return data

def get_data(paths):
    path = Path(str(paths))
    files = Path(path).glob('*.csv') 
    dfs = [pd.read_csv(f) for f in files]

    """
    TODO:
    Why do we need preproces_data folder?
    """


    # Combine the list of dataframes
    df = preproces_data(pd.concat(dfs, ignore_index=True))

    # Add a new column with each year the row is from
    df['Source'] = np.repeat([f'20{i+17}' for i in range(len(dfs))], [len(df) for df in dfs])

    # Making partition of the data - could probably be done in one or two lines
    df[df['Source'] == str(2017)].to_csv(str(paths)+str('/Preprocessed Data/DF17.csv'))
    df[df['Source'] == str(2018)].to_csv(str(paths)+str('/Preprocessed Data/DF18.csv'))
    df[df['Source'] == str(2019)].to_csv(str(paths)+str('/Preprocessed Data/DF19.csv'))
    df[df['Source'] == str(2020)].to_csv(str(paths)+str('/Preprocessed Data/DF20.csv'))
    df[df['Source'] == str(2021)].to_csv(str(paths)+str('/Preprocessed Data/DF21.csv'))
    df[df['Source'] == str(2022)].to_csv(str(paths)+str('/Preprocessed Data/DF22.csv'))
    return df