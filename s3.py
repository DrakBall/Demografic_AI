import requests
import s3
import os

def descargar():
    arrayUrl = []

    # Añadir las URLs de los archivos
    arrayUrl.append("Modificar/barcelona.csv")
    arrayUrl.append("Modificar/catalunia.csv")
    arrayUrl.append("Modificar/tarragones.csv")
    arrayUrl.append("Nacimiento_Defuncion/Barcelona.csv")
    arrayUrl.append("Nacimiento_Defuncion/Catalunia.csv")
    arrayUrl.append("Nacimiento_Defuncion/Tarragones.csv")
    arrayUrl.append("CatMigr.csv")
    arrayUrl.append("TarMigr.csv")
    arrayUrl.append("censoTGN.csv")
    arrayUrl.append("Media_edad_pobl.csv")
    arrayUrl.append("mortaldat.csv")
    arrayUrl.append("natalitat.csv")
    arrayUrl.append("pronostico_mort.csv")
    arrayUrl.append("pronostico_nat.csv")

    # Crear las carpetas específicas si no existen
    if not os.path.exists("Modificar"):
        os.makedirs("Modificar")

    if not os.path.exists("Nacimiento_Defuncion"):
        os.makedirs("Nacimiento_Defuncion")

    # Usar un bucle para iterar sobre la lista arrayUrl
    for archivo in arrayUrl:
        url = f"https://mazorca.s3.us-east-1.amazonaws.com/{archivo}"  # URL completa del archivo
        response = requests.get(url)

        if response.status_code == 200:
            # Comprobar si la URL incluye una carpeta antes del archivo
            if '/' in archivo:
                # Si tiene una barra, pertenece a una carpeta específica
                carpeta_destino = archivo.split("/")[0]
            else:
                # Si no tiene barra, lo guardamos en la carpeta actual
                carpeta_destino = "."  # Usamos la carpeta actual

            # Crear la carpeta de destino si no existe
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            # Construir la ruta completa para guardar el archivo en la carpeta correspondiente
            ruta_archivo = os.path.join(carpeta_destino, os.path.basename(archivo))

            # Guardar el archivo en la carpeta correspondiente
            with open(ruta_archivo, "wb") as file:
                file.write(response.content)
            print(f"Descarga completa de {archivo} en la carpeta '{carpeta_destino}'")
        else:
            print(f"Error al descargar {archivo}: {response.status_code}")

def cargar():
    import boto3
    import os

    # Crear un cliente de S3 usando boto3
    s3 = boto3.client('s3')


    # Nombre del bucket de destino
    bucket_name = 'mazorca'

    # Lista de archivos que deseas subir
    arrayUrl = [
        "Modificar/barcelona.csv",
        "Modificar/cataluna.csv",
        "Modificar/tarragones.csv",
        "Nacimiento_Defuncion/Barcelona.csv",
        "Nacimiento_Defuncion/Catalunia.csv",
        "Nacimiento_Defuncion/Tarragones.csv",
        "CatMigr.csv",
        "TarMigr.csv",
        "censoTGN.csv",
        "Media_edad_pobl.csv",
        "mortaldat.csv",
        "natalitat.csv",
        "pronostico_mort.csv",
        "pronostico_nat.csv"
    ]

    # Usar un bucle para iterar sobre los archivos
    for archivo in arrayUrl:
        # Construir la ruta local completa del archivo
        ruta_archivo_local = archivo

        # Comprobar si el archivo existe en el sistema local
        if os.path.exists(ruta_archivo_local):
            # Subir el archivo a S3 (si el archivo tiene una carpeta, mantenla en la estructura del bucket)
            try:
                s3.upload_file(ruta_archivo_local, bucket_name, archivo)
                print(f"Archivo {archivo} subido exitosamente a S3.")
            except Exception as e:
                print(f"Error al subir el archivo {archivo}: {e}")
        else:
            print(f"El archivo {archivo} no existe en la ruta local.")
