## 참고 URL https://www.kaggle.com/datasets/columbia2131/otto-chunk-data-inparquet-format
import os

import numpy as np
import pandas as pd

from pathlib import Path
from tqdm import tqdm

# kaggle 실행시
# data_path = Path('/kaggle/input/otto-recommender-system/')
data_path = Path('.')
chunksize = 100_000

# train_set
chunks = pd.read_json(data_path / 'train.jsonl', lines=True, chunksize=chunksize)
os.mkdir('train_parquet')

for e, chunk in enumerate(tqdm(chunks, total=129)):
    event_dict = {
        'session': [],
        'aid': [],
        'ts': [],
        'type': [],
    }

    for session, events in zip(chunk['session'].tolist(), chunk['events'].tolist()):
        for event in events:
            event_dict['session'].append(session)
            event_dict['aid'].append(event['aid'])
            event_dict['ts'].append(event['ts'])
            event_dict['type'].append(event['type'])

    # save DataFrame
    start = str(e * chunksize).zfill(9)
    end = str(e * chunksize + chunksize).zfill(9)
    pd.DataFrame(event_dict).to_parquet(f"train_parquet/{start}_{end}.parquet")

# test set
chunks = pd.read_json(data_path / 'test.jsonl', lines=True, chunksize=chunksize)
os.mkdir('test_parquet')

for e, chunk in enumerate(tqdm(chunks, total=17)):
    event_dict = {
        'session': [],
        'aid': [],
        'ts': [],
        'type': [],
    }

    for session, events in zip(chunk['session'].tolist(), chunk['events'].tolist()):
        for event in events:
            event_dict['session'].append(session)
            event_dict['aid'].append(event['aid'])
            event_dict['ts'].append(event['ts'])
            event_dict['type'].append(event['type'])

    # save DataFrame
    start = str(e * chunksize).zfill(9)
    end = str(e * chunksize + chunksize).zfill(9)
    pd.DataFrame(event_dict).to_parquet(f"test_parquet/{start}_{end}.parquet")
