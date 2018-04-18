import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
import seaborn as sbn

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
    # index_data['NIKKEI225_diff'] = index_data['NIKKEI225'].diff()
    # index_data['DJIA_diff'] = index_data['DJIA'].diff()

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

    # print(index_data.describe())
    #           NIKKEI225          DJIA  NIKKEI225_diff    DJIA_diff
    # count   2610.000000   2610.000000     2609.000000  2609.000000
    # mean   13793.675766  14833.273134        3.396409     4.621725
    # std     4408.360800   4264.577273      197.380024   144.118797
    # min     7054.980000   6547.050000    -1286.330000 -1175.210000
    # 25%     9637.262500  11413.367500      -82.100000   -51.280000
    # 50%    13692.115000  14639.075000        0.000000     4.490000
    # 75%    17390.917500  17744.642500      101.130000    72.090000
    # max    24124.150000  26616.710000     1343.430000   936.420000

    # index_data['NIKKEI225_ratio'] = index_data['NIKKEI225_diff'] / index_data['NIKKEI225']
    print("Correlation: \n", index_data.corr())
    print("Standard Deviation: \n", index_data.std())
    mean = index_data.mean()
    print("Mean: \n", mean)
    cov = index_data.cov()
    print("cov: \n", cov)
    std = np.sqrt(np.diag(cov))
    print("std: \n", std)

    plt.figure(figsize=(10, 6))
    plt.scatter(std, mean, c=mean / std, marker='o')
    plt.grid(True)
    plt.xlabel('expected volatility')
    plt.ylabel('expected return')
    plt.show()

    def min_func(weights):
        return np.dot(weights.T, np.dot(cov, weights))

    x0 = [0.1, 0.9]
    # print(x0)
    target_return = 0.1
    cons = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'ineq', 'fun': lambda x: np.sum(mean * x) - target_return}]
    bnds = [(0, None)] * len(mean)
    opts = sco.minimize(fun=min_func, x0=x0, method='SLSQP', bounds=bnds, constraints=cons)
    print(opts['x'])
    print(opts['success'])


if __name__ == '__main__':
    main()