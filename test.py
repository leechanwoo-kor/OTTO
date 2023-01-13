import pandas as pd
from glob import glob

files = sorted(glob('./train_parquet/*'))
m_df = pd.DataFrame()

for path in files:
    df = pd.read_parquet(path)
    g_df = df.groupby('session').agg(list).reset_index()
    m_df = pd.concat([m_df, g_df])

