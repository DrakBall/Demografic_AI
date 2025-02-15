import pandas as pd
import glob

def modificar_valores():
    archivos_csv = glob.glob("Modificar/*.csv")
    print(archivos_csv)

    for archivo in archivos_csv:
        df = pd.read_csv(archivo, sep=";", header=None)  # Asegúrate de que el separador es correcto

        df.columns = ["Año", "municipio", "edad quinquenal", "sexo", "concepto", "estado", "valor"]  # Column name

        valor_str = str(df.loc[2, "valor"])
        if "." in valor_str or "," in valor_str:  # Comprobar si hay coma
            print("El valor es un por ciento.")
        else:
            año_mirar = df.loc[0, "Año"]

            df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
            df_año = df[df["Año"] == año_mirar]
            total_año = df_año[df_año["edad quinquenal"] == "total"]

            index = 0
            while len(df_año) != 0:
                num_total = total_año["valor"]
                poblacion_total = num_total.iloc[2]

                longitud = len(df_año["valor"])

                for i in range(longitud - 1):
                    valor_actual = df_año.iloc[i]["valor"]
                    porciento = (valor_actual * 100) / poblacion_total
                    df.at[index, "valor"] = porciento
                    index += 1
                index += 1
                año_mirar += 1

                df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
                df_año = df[df["Año"] == año_mirar]
                total_año = df_año[df_año["edad quinquenal"] == "total"]

        df.to_csv(archivo, sep=";", index=False, header=False)
