import pandas as pd

def load_nikkei225():
    data = pd.read_csv('../data/nikkei225.csv')
    return data

def load_daw():
    data = pd.read_csv('../data/daw.csv')
    return data