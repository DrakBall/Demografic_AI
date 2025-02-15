import pandas as pd
import glob

def crecimiento_neto():
    archivos_csv = glob.glob("Nacimiento_Defuncion/*.csv")
    print(archivos_csv)

    for archivo in archivos_csv:
        df = pd.read_csv(archivo, sep=';', header=None)  # Lee el archivo sin encabezado
        print(f"Archivo: {archivo} - Columnas detectadas: {len(df.columns)}")
        if df.iloc[0].dtype == object:
            print(f"El archivo {archivo} ya tiene encabezados, se omite la modificación.")
            continue  # Saltar este archivo
        df.columns = ["Año", "Nacimiento", "Defunciones", "Neto"]  # Column name

        fila_actual = 0
        ultima_fila = df.last_valid_index()  # Última fila con valores

        while fila_actual <= ultima_fila:
            nacimientos = df.at[fila_actual, "Nacimiento"]
            Defunciones = df.at[fila_actual, "Defunciones"]

            neto = nacimientos - Defunciones

            df.at[fila_actual, "Neto"] = neto
            fila_actual += 1
    df.to_csv(archivo, sep=";", index=False, header=None)