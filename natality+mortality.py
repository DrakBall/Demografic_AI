import timeGPT as ia
import csvTreatment as ct
import hacer_grafico as hg


df_nat=ct.csv_treatment("natalitat.csv", "Total")
pronostico_nat=ia.generate_grafic(df_nat, "Total", "api-key")

df_mort=ct.csv_treatment("mortaldat.csv", "Total")
pronostico_mort=ia.generate_grafic(df_mort, "Total", "api-key")

ct.csv_save(pronostico_nat, "pronostico_nat.csv")
ct.csv_save(pronostico_mort, "pronostico_mort.csv")

hg.hacer_grafico("natalitat", df_nat, pronostico_nat, "Total")
hg.hacer_grafico("mortaldat", df_mort, pronostico_mort, "Total")