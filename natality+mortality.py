import timeGPT as ia
import csvTreatment as ct
import hacer_grafico as hg


df_nat=ct.csv_treatment("natalitat.csv", "Total")
pronostico_nat=ia.generate_grafic(df_nat, "Total", "nixak-MNEV6YUxCQmSyIZjfKKmuBMJYQQdacQDh1MPPkpgoQxH2YgNdWR35yl4KpVm3sbt1wnI5FXv7evbax9O")

df_mort=ct.csv_treatment("mortaldat.csv", "Total")
pronostico_mort=ia.generate_grafic(df_mort, "Total", "nixak-MNEV6YUxCQmSyIZjfKKmuBMJYQQdacQDh1MPPkpgoQxH2YgNdWR35yl4KpVm3sbt1wnI5FXv7evbax9O")

ct.csv_save(pronostico_nat, "pronostico_nat.csv")
ct.csv_save(pronostico_mort, "pronostico_mort.csv")

hg.hacer_grafico(df_nat, pronostico_nat, "Total")
hg.hacer_grafico(df_mort, pronostico_mort, "Total")