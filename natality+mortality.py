import timeGPT as ia
import csvTreatment as ct
import hacer_grafico as hg
import matplotlib.pyplot as plt

df_nat=ct.csv_treatment("natalitat.csv", "Total")
pronostico_nat=ia.generate_grafic(df_nat, "Total", "nixak-MNEV6YUxCQmSyIZjfKKmuBMJYQQdacQDh1MPPkpgoQxH2YgNdWR35yl4KpVm3sbt1wnI5FXv7evbax9O")

df_mort=ct.csv_treatment("mortaldat.csv", "Total")
pronostico_mort=ia.generate_grafic(df_mort, "Total", "nixak-MNEV6YUxCQmSyIZjfKKmuBMJYQQdacQDh1MPPkpgoQxH2YgNdWR35yl4KpVm3sbt1wnI5FXv7evbax9O")

ct.csv_save(pronostico_nat, "pronostico_nat.csv")
ct.csv_save(pronostico_mort, "pronostico_mort.csv")

hg.hacer_grafico("natalitat", df_nat, pronostico_nat, "Total")
hg.hacer_grafico("mortaldat", df_mort, pronostico_mort, "Total")

plt.figure(figsize=(10, 6))
plt.plot(df_nat['Año'], df_nat['Total'], label='Nacidos_Actual')
plt.plot(pronostico_nat['Año'], pronostico_nat['TimeGPT'], label='Nacidos_Forecast', linestyle='--')
plt.plot(df_mort['Año'], df_mort['Total'], label='Defunciones_Actual')
plt.plot(pronostico_mort['Año'], pronostico_mort['TimeGPT'], label='Defunciones_Forecast', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Natalitat i Mortaldat')
plt.legend()
plt.grid(True)
plt.savefig("natal_mortal.png", dpi=300)

df_int = ct.csv_inmigration("TarMigr.csv", "Saldo migratori (interna)")
pronostico_int = ia.generate_grafic(df_int, "Saldo migratori (interna)", "api-key")

df_ext = ct.csv_inmigration("TarMigr.csv", "Saldo migratori (externa)")
pronostico_ext = ia.generate_grafic(df_ext, "Saldo migratori (externa)", "api-key")

df_tot = ct.csv_inmigration("TarMigr.csv", "Saldo migratori total")
pronostico_tot = ia.generate_grafic(df_tot, "Saldo migratori total", "api-key")

plt.figure(figsize=(10, 6))
plt.plot(df_int['Año'], df_int['Saldo migratori (interna)'], label='Interno Actual')
plt.plot(pronostico_nat['Año'], pronostico_nat['TimeGPT'], label='Interno Forecast', linestyle='--')
plt.plot(df_ext['Año'], df_ext['Saldo migratori (externa)'], label='Externo Actual')
plt.plot(pronostico_ext['Año'], pronostico_ext['TimeGPT'], label='Externo Forecast', linestyle='--')
plt.plot(df_tot['Año'], df_tot['Saldo migratori total'], label='Total Actual')
plt.plot(pronostico_tot['Año'], pronostico_tot['TimeGPT'], label='Total Forecast', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Saldo Migratorio')
plt.legend()
plt.grid(True)
plt.savefig("migracioTag.png", dpi=300)

df_edad = ct.csv_edad("Media_edad_pobl.csv")
pronostico_edad = ia.generate_grafic(df_edad, "edad", "api-key")

hg.hacer_grafico("edad", df_edad, pronostico_edad, "edad")

df_censo = ct.csv_2("censoTGN.csv", "Total")
pronostico_censo = ia.generate_grafic(df_censo, "Total", "api-key")
hg.hacer_grafico("censo", df_censo, pronostico_censo, "Total")

plt.figure(figsize=(10, 6))
plt.plot(df_tot['Año'], df_tot['Saldo migratori total'], label='Total Actual')
plt.plot(pronostico_tot['Año'], pronostico_tot['TimeGPT'], label='Total Forecast', linestyle='--')
plt.plot(df_nat['Año'], df_nat['Total'], label='Nacidos_Actual')
plt.plot(pronostico_nat['Año'], pronostico_nat['TimeGPT'], label='Nacidos_Forecast', linestyle='--')
plt.plot(df_mort['Año'], df_mort['Total'], label='Defunciones_Actual')
plt.plot(pronostico_mort['Año'], pronostico_mort['TimeGPT'], label='Defunciones_Forecast', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Relacio natalitat-mortaldat-inmigracio')
plt.legend()
plt.grid(True)
plt.savefig("natalitat_mortaldat_inmigracio.png", dpi=300)
