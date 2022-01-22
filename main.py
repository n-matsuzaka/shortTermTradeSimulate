import pandas as pd

if __name__ == '__main__':
    # read price csv data from google finance
    df = pd.read_csv("price_data.csv")
    # select stocks to buy for each day

