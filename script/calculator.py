import pandas as pd
import data_loader


def main():
    nikkei = data_loader.load_nikkei225()
    print(nikkei.head())
    daw = data_loader.load_daw()
    print(daw.head())

if __name__ == '__main__':
    main()