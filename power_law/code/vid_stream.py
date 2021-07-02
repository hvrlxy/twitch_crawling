import pandas as pd
import numpy as np
import math

#read all streams
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
total_stream = stream['stream_id'].unique()

#read the stream with videos
df = pd.read_csv('vid.csv')
df = pd.DataFrame(df)

mapping = {df.columns[0]: 'vid_id',
        df.columns[1]: 'stream_id', df.columns[2]: 'user_id',
           df.columns[3]: 'title', df.columns[4]: 'description',
           df.columns[5]: 'view_count', df.columns[6]: 'lganguage',
           df.columns[7]: 'type',
           df.columns[8]:'duration', df.columns[9]:'published_at'}

df = df.rename(columns=mapping)

df['published_at'] = pd.to_datetime(df['published_at'])

mapping = {}

for stream in total_stream:
  st_df = df.loc[df['stream_id'] == stream]
  no_vids = len(st_df['vid_id'].unique())
  if no_vids not in mapping:
    mapping[no_vids] = 1
  else:
    mapping[no_vids] += 1

#plotting the pie chart
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
num_vids = list(mapping.keys())
frequency = [mapping[i] for i in num_vids]
ax.pie(frequency, labels = num_vids,autopct='%1.2f%%')

plt.title("Number of Streams With Videos Uploaded")
plt.show()


