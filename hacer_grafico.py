import matplotlib.pyplot as plt

def hacer_grafico(nombre_grafico, df, pronostico, columna):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Año'], df[columna], label='Actual')
    plt.plot(pronostico['Año'], pronostico['TimeGPT'], label='Forecast', linestyle='--')
    plt.xlabel('Year')
    plt.ylabel('Total')
    plt.title('Forecast vs Actual')
    plt.legend()
    plt.grid(True)
    #plt.show()
    nombre=nombre_grafico+".png"
    plt.savefig(nombre, dpi=300)
    return None