# see whether if many stream would gain more user than less stream with long streaming period
# - look at the average number of viewers per stream
# - x-axis: the number of hours stream
# - y-axis: average number of viewers per stream

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
stream['current_hour'] = stream['current_time'].apply(lambda x: x.hour)

unique_user = list(stream['user_id'].unique())

num_streams = []
average_viewers = []

for user in unique_user:
	user_pd = stream.loc[stream['user_id'] == user]
	unique_stream = user_pd['stream_id'].unique()
	num = 0
	count = 0
	for st in unique_stream:
		stream_pd = user_pd.loc[user_pd['stream_id'] == st]
		if len(stream_pd) > 1:
			stream_np = stream_pd.to_numpy()
			count += (stream_np[len(stream_np) - 1, 6] - stream_np[0, 6])
			num += len(stream_pd) * 0.5
		else:
			num -= 1
	if num > 0:
		num_streams.append(num)
		average_viewers.append(count)

import matplotlib.pyplot as plt

# This will plot a simple scatter chart
plt.scatter(num_streams, average_viewers)

#name the axis
plt.xlabel('# of hours')
plt.ylabel('# of viewers')
  
# Title to the plot
# plt.title("Average Viewers for Videos Started At (Spanish)")

plt.title("Number Of Hours Stream Per Week vs Viewers")
  
plt.show()

