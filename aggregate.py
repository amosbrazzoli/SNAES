import os
import pandas as pd
from tqdm import tqdm

f = []

for (dirpath, dirnames, filenames) in os.walk("data"):
    f.extend(filenames)

EXCLUDE = ["EDIANAGRAFESTA20181920180901.csv"]


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

df.to_excel("SNAES-1819.xlsx")