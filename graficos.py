import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

ruta_csv = glob.glob("Modificar/*.csv")
for archivo in ruta_csv:
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]
    df = pd.read_csv(archivo, sep=";")  # Asegúrate de que el separador es correcto

    año_mirar = pd.to_numeric(df.iloc[0]["Año"])
    ultimo_año = pd.to_numeric(df.iloc[-1]["Año"])

    while año_mirar in range (año_mirar, ultimo_año + 1):
        df_año = df[(df["Año"] == año_mirar) & (df["edad quinquenal"] != "total") & (df["sexo"] == "total")]
        df_atus = df_año.groupby("edad quinquenal")["valor"].sum().reset_index()
        plt.figure(figsize=(10,8))
        sns.barplot(x="edad quinquenal", y="valor", data=df_atus, palette="Blues")


        plt.xlabel("Edad Quincenal")
        plt.ylabel("Total Valor")
        plt.title("Edad Poblacional del "+str(año_mirar)+ " en la region"+str(nombre_base))
        plt.xticks(rotation=-90)  # Rotar etiquetas del eje X si hay muchos años
        plt.grid(axis="y", linestyle="--", alpha=0.7)  # Líneas en el fondo para mejorar la visibilidad

        carpeta_salida = "Graficos_poblacion"  # Nombre de la carpeta donde quieres guardar las imágenes

        # Crear la carpeta si no existe
        os.makedirs(carpeta_salida, exist_ok=True)

        plt.savefig(os.path.join(carpeta_salida, f"{nombre_base}_{año_mirar}.png"))

        plt.close()
        año_mirar+=1