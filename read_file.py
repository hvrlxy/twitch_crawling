import pandas as pd
import numpy as np
import math
import datetime

stream = pd.read_csv('../data/stream_week1.csv')
stream = pd.DataFrame(stream)

mapping = {stream.columns[0]: 'stream_id',
           stream.columns[1]: 'user_id', stream.columns[2]: 'start_time',
           stream.columns[3]: 'game_name', stream.columns[4]: 'game_id',
           stream.columns[5]: 'language', stream.columns[6]: 'viewer',
           stream.columns[7]: 'followers',
           stream.columns[8]:'current_time'}

stream = stream.rename(columns=mapping)

stream['current_time'] = pd.to_datetime(stream['current_time'])

stream = stream.loc[stream['current_time'] < datetime.datetime(2021, 6, 18)]

print(stream)

stream2 = pd.read_csv('../data/stream_data_week1_Junming.csv')
stream2 = pd.DataFrame(stream2)
stream = stream.append(stream2)

stream3 = pd.read_csv('../data/stream_data_week2_Junming.csv')
stream3 = pd.DataFrame(stream3)
stream = stream.append(stream3)

stream4 = pd.read_csv('../data/stream_week2+.csv')
stream4 = pd.DataFrame(stream4)
stream = stream.append(stream4)

stream['current_time'] = pd.to_datetime(stream['current_time'])
