import matplotlib.pyplot as plt
from nixtla import NixtlaClient
import csvTreatment as ct

df=ct.csv_treatment("natalitat.csv")

nixtla_client = NixtlaClient(api_key='api-key') # replace 'api-key' with your API key

if nixtla_client.validate_api_key():
    print("Valid API key.")
else:
    print("Invalid API key.")

# Forecast
pronostico = nixtla_client.forecast(
    df=df,
    h=10,  # Forecast horizon
    freq='YE',  # Frequency of the data
    time_col='Any',  # Timestamp column
    target_col='Total'  # Value column
)

# Grafical representation
plt.figure(figsize=(10, 6)) # set figure size
plt.plot(df['Any'], df['Total'], label='Actual') # Actual data
plt.plot(pronostico['Any'], pronostico['TimeGPT'], label='Forecast', linestyle='--') # Forecast data
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Forecast vs Actual')
plt.legend() # show legend
plt.grid(True) # show grid
plt.show()
