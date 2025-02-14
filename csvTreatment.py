import pandas as pd
import csv

def csv_treatment(csv, column):

    df = pd.read_csv(csv, sep=';', header=None) # read csv file
    df.columns = ["Año", "Homes", "Dones", "Total"]  # Column names
    df = df.dropna() # drop NaN values

    df["Año"] = pd.to_datetime(df["Año"], format="%Y") # convert Any column to datetime

    columnas_seleccionadas = ["Año", column] # select columns
    df = df[columnas_seleccionadas]

    return df

def csv_save(pronostico, nombre):
    with open(nombre, mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(10):
            writer.writerow([pronostico.iloc[i, 0], pronostico.iloc[i, 1]])
    return None