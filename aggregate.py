import os
import pandas as pd
from tqdm import tqdm

f = []

for (dirpath, dirnames, filenames) in os.walk("data"):
    f.extend(filenames)

EXCLUDE = ["EDIANAGRAFESTA20181920180901.csv","SCUANAGRAFESTAT20212220210901.csv"]

for e in EXCLUDE:
    f.remove(e)


df = pd.read_csv("data/{}".format(EXCLUDE[0]))
SORTER = ["CODICEEDIFICIO", "CODICESCUOLA", "ANNOSCOLASTICO"]
df = df.sort_values(by=SORTER)


for file in tqdm(f):
    if file.endswith(".csv"):
        print(file)
        t_df = pd.read_csv("data/{}".format(file))
        t_df = t_df.sort_values(by=SORTER)
        df = pd.merge(df, t_df, on=SORTER, how="left")
        print(df.shape, df.memory_usage().sum() / 1024 ** 2, sep="\t")

# Aggiunge anagrafica sul tipo di scuola
ana_df = pd.read_csv("data/{}".format(EXCLUDE[1]))
ana_df = ana_df.sort_values(by=["CODICESCUOLA"])
PURGE = ["ANNOSCOLASTICO",
            "INDIRIZZOSCUOLA", 
            "CAPSCUOLA",
            "DESCRIZIONECOMUNE",
            "CODICECOMUNESCUOLA",
            ]
ana_df = ana_df.drop(PURGE, axis=1)
df = pd.merge(ana_df, df, on=["CODICESCUOLA"], how="left")

print("Saving will take some time ... please wait")
df.to_excel("SNAES-1819.xlsx")
print("Done")