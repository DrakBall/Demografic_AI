from nixtla import NixtlaClient

def generate_grafic(df, column, api):


    nixtla_client = NixtlaClient(api_key=api)

    if nixtla_client.validate_api_key():
        print("Valid API key.")
    else:
        print("Invalid API key.")

    # Forecast
    pronostico = nixtla_client.forecast(
        df=df,
        h=10,  # Forecast horizon
        freq='YE',  # Frequency of the data
        time_col='Año',  # Timestamp column
        target_col=column  # Value column
    )

    return pronostico


