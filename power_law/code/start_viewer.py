import pandas as pd
import numpy as np
import math

stream = pd.read_csv('../data/stream_week1.csv')
stream = pd.DataFrame(stream)

mapping = {stream.columns[0]: 'stream_id',
           stream.columns[1]: 'user_id', stream.columns[2]: 'start_time',
           stream.columns[3]: 'game_name', stream.columns[4]: 'game_id',
           stream.columns[5]: 'language', stream.columns[6]: 'viewer',
           stream.columns[7]: 'followers',
           stream.columns[8]:'current_time'}

stream = stream.rename(columns=mapping)

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

#take the ids of all the streams
unique_stream = stream['stream_id'].unique()

start_view = []

for st in unique_stream:
    st_df = stream.loc[stream['stream_id'] == st]
    st_nd = st_df.to_numpy()
    print(st)
    if str(st) == 'nan' or str(st_nd[0, 6]) == 'nan':
        continue
    else:
        start_view.append(max(1,int(st_nd[0, 6])))

start_view = [max(1, math.floor(i/50) * 50) for i in start_view]

mapping = {}
for i in start_view:
    if i in mapping:
        mapping[i] += 1
    else:
        mapping[i] = 1

import matplotlib.pyplot as plt

x = list(mapping.keys())
y = [mapping[i] for i in x]

x = [math.log10(float(i)) for i in x]
y = [math.log10(float(i)) for i in y]

# This will plot a simple scatter chart
plt.scatter(x, y)

#name the axis
plt.xlabel('# of viewers')
plt.ylabel('# frequency')
  
# Title to the plot
plt.title("Distribution of Viewers Tuned In At the Start")
  
plt.show()