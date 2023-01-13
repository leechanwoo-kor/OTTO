## 참고 URL https://www.kaggle.com/datasets/columbia2131/otto-chunk-data-inparquet-format
#import
import os

import numpy as np
import pandas as pd

from pathlib import Path
from tqdm import tqdm

# kaggle 실행시
# data_path = Path('/kaggle/input/otto-recommender-system/')

def jsonl_to_parquet(i_type):
    data_path = './input/'
    chunksize = 100_000

    data_name = i_type + '.jsonl'

    chunks = pd.read_json(data_path + data_name, lines=True, chunksize=chunksize)
    if os.path.isdir(i_type + '_parquet'):
        os.rmdir(i_type + '_parquet')
        os.mkdir(i_type + '_parquet')
    else:
        os.mkdir(i_type + '_parquet')

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
        pd.DataFrame(event_dict).to_parquet(f"{i_type}_parquet/{start}_{end}.parquet")


# train_set
jsonl_to_parquet('train')

# test set
jsonl_to_parquet('test')
