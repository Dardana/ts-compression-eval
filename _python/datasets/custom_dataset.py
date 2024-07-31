from . import paths
import pandas as pd
import os
from joblib import Memory
import numpy as np
from .. import files

from . import viz
from . import paths

_memory = Memory('./')
DATA_DIR = paths.CUSTOM_DATA
DATA_FILE = 'd1.csv'
FIG_SAVE_DIR =os.path.join('figs', 'custom_data')


COL_t = ['time']
COL = ['id_station']
COLS_DATA = ['s{}'.format(i) for i in range(100)]
COLS = COL_t + COLS_DATA
COLS_ALL = COLS + COL

class Custom(object):

    def __init__(self, path):
        data = _load_data(path)
        self.path = path
        self.name = os.path.basename(path).split('.')[0]
        self.sampleTimes =pd.to_datetime(data['time']).apply(lambda x: int(x.timestamp()))
        self.data = data[COLS_DATA].values.astype(np.float32)


def all_recordings():
    recordings = []
    for file_name in os.listdir(DATA_DIR):
         if file_name.endswith('.csv'):  # Ensure only CSV files are processed
              path = os.path.join(DATA_DIR, file_name)
              recordings.append(Custom(path))
    return recordings


@_memory.cache
def _load_data(path):
    df = pd.read_csv(path)
    df = df.drop(columns=['id_station'])
    print(df[COLS])
    return df[COLS]

def _datetimes_to_unix_timestamps(datetimes):
    # https://stackoverflow.com/q/34038273
    return (datetimes.astype(np.int64) / 1e6).astype(np.uint64)


def _datetime_strs_to_unix_timestamps(strs):
    return _datetimes_to_unix_timestamps(pd.to_datetime(strs, errors='coerce',  dayfirst=False))

def main():
    recordings = all_recordings()
    for recording in recordings:
        fig_save_path = os.path.join(FIG_SAVE_DIR, recording.name)
        os.makedirs(fig_save_path, exist_ok=True)
        #viz.save_fig_png([recording], interval_len=10000, savedir=fig_save_path)


if __name__ == '__main__':
    main()