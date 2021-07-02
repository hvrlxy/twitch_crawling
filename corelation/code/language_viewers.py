import pandas as pd
import numpy as np
import math
import datetime

stream = pd.read_csv('../../data/stream_week1.csv')
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

stream2 = pd.read_csv('../../data/stream_data_week1_Junming.csv')
stream2 = pd.DataFrame(stream2)
stream = stream.append(stream2)

stream3 = pd.read_csv('../../data/stream_data_week2_Junming.csv')
stream3 = pd.DataFrame(stream3)
stream = stream.append(stream3)

stream4 = pd.read_csv('../../data/stream_week2+.csv')
stream4 = pd.DataFrame(stream4)
stream = stream.append(stream4)

stream['current_time'] = pd.to_datetime(stream['current_time'])

# print(stream['language'].unique())
# exit()
#pick the language
# [it' 'zh' 'tr' 'es' 'pl' 'bg' 'other'
#  'th' 'sv' 'ar' 'hu' 'cs' 'el' 'nl' 'fi' 'ms' 'no' 'zh-hk' 'da' 'uk' 'ro'
#  'sk' 'id']
current_language = 'es'

stream = stream.loc[stream['language'] == current_language]

stream['start_time'] = pd.to_datetime(stream['start_time'])
stream['start_hour'] = stream['start_time'].apply(lambda x: x.hour)

# x = list(stream['start_hour'])

stream['current_hour'] = stream['current_time'].apply(lambda x: x.hour)

x = list(stream['current_hour'])
y = list(stream['viewer'])

import matplotlib.pyplot as plt

# This will plot a simple scatter chart
plt.scatter(x, y)

#name the axis
plt.xlabel('time in hour (utc) ')
plt.ylabel('# of viewers')
  
# Title to the plot
# plt.title("Average Viewers for Videos Started At (Spanish)")

plt.title("Viewers and Streaming Hours (Spanish)")
  
plt.show()