import pandas as pd

def csv_treatment(csv):

    df = pd.read_csv(csv, sep=';', header=None) # read csv file
    df.columns = ["Any", "Homes", "Dones", "Total"]  # Column names
    df = df.dropna() # drop NaN values

    df["Any"] = pd.to_datetime(df["Any"], format="%Y") # convert Any column to datetime

    columnas_seleccionadas = ["Any", "Total"] # select columns
    df = df[columnas_seleccionadas]

    return df