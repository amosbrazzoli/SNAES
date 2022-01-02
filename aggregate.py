# %%
import os
import pandas as pd
from tqdm import tqdm

f = []

for (dirpath, dirnames, filenames) in os.walk("data"):
    f.extend(filenames)

EXCLUDE = ["EDIANAGRAFESTA20181920180901.csv"]

f

# %%
for e in EXCLUDE:
    f.remove(e)

f

# %%
df = pd.read_csv("data/{}".format(EXCLUDE[0]))
df

# %%
for file in tqdm(f):
    if file.endswith(".csv"):
        print(file)
        t_df = pd.read_csv("data/{}".format(file))
        df = pd.merge(df, t_df, on="CODICESCUOLA")
        del t_df
        print(df.memory_usage)

# %%
df
