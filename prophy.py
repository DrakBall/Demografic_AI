from prophet import Prophet
import matplotlib.pyplot as plt
import csvTreatment as ct

df=ct.csv_treatment("natalitat.csv")

df_prophet = df.rename(columns={"Any": "ds", "Total": "y"}) # rename columns

model = Prophet() # create model
model.fit(df_prophet) # fit model

future = model.make_future_dataframe(periods=10, freq="Y") # create future dataframe
forecast = model.predict(future) # predict future data

# Grafical representation
model.plot(forecast)
plt.show()




