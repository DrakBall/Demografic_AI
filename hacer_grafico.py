import matplotlib.pyplot as plt

def hacer_grafico(nombre_grafico, data_frame, pronostico, columna):

    plt.figure(figsize=(10, 6))
    plt.plot(data_frame['Año'], data_frame[columna], label='Actual')
    plt.plot(pronostico['Año'], pronostico['TimeGPT'], label='Forecast', linestyle='--')
    plt.xlabel('Year')
    plt.ylabel('Total')
    plt.title(nombre_grafico)
    plt.legend()
    plt.grid(True)
    nombre=nombre_grafico+".png"
    plt.savefig(nombre, dpi=300)
    return None