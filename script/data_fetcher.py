import pandas_datareader.data as pdr
import datetime


def fetch_nikkei225(start, end):
    data = pdr.DataReader('NIKKEI225', 'fred', start, end)
    return data


def store(df, filename):
    df.to_csv("../data/{}".format(filename))


def fetch_daw(start, end):
    data = pdr.DataReader('DJIA', 'fred', start, end)
    return data

def main():
    start = datetime.datetime(2000, 1, 4)
    end = datetime.datetime(2018, 4, 16)
    # data = fetch_nikkei225(start, end)
    data = fetch_daw(start, end)
    store(data, 'daw.csv')

if __name__ == "__main__":
    main()