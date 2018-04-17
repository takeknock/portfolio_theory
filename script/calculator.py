import pandas as pd
import numpy as np
import data_loader

def main():
    nikkei = data_loader.load_nikkei225()
    # print(nikkei.head())
    daw = data_loader.load_daw()
    # print(daw.head())

    # concatinate on DATE
    index_data = pd.merge(nikkei, daw, on='DATE')
    # print(index_data.head())

    # fill na with before data
    index_data['NIKKEI225'] = index_data['NIKKEI225'].fillna(method='ffill')
    index_data['DJIA'] = index_data['DJIA'].fillna(method='ffill')

    # diff
    index_data['NIKKEI225_diff'] = index_data['NIKKEI225'].diff()
    index_data['DJIA_diff'] = index_data['DJIA'].diff()

    # print(index_data.isnull().sum())
    # before fill na
    # DATE 0
    # NIKKEI225 159
    # DJIA 91
    # NIKKEI225_diff 282
    # DJIA_diff 182

    # after fill na
    # DATE 0
    # NIKKEI225 0
    # DJIA 0
    # NIKKEI225_diff 1
    # DJIA_diff 1

    print(index_data.describe())
    #           NIKKEI225          DJIA  NIKKEI225_diff    DJIA_diff
    # count   2610.000000   2610.000000     2609.000000  2609.000000
    # mean   13793.675766  14833.273134        3.396409     4.621725
    # std     4408.360800   4264.577273      197.380024   144.118797
    # min     7054.980000   6547.050000    -1286.330000 -1175.210000
    # 25%     9637.262500  11413.367500      -82.100000   -51.280000
    # 50%    13692.115000  14639.075000        0.000000     4.490000
    # 75%    17390.917500  17744.642500      101.130000    72.090000
    # max    24124.150000  26616.710000     1343.430000   936.420000

    index_data['NIKKEI225_ratio'] = index_data
    print(index_data.corr())
    print(index_data.std())
    print(index_data.mean())

if __name__ == '__main__':
    main()