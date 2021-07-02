# this program graph the average increase in follower in a stream, where the x axis is the number of hours
# into the stream, and the y axis is the average increase in followers

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

unique_stream = stream['stream_id'].unique()

# print(stream.loc[stream['stream_id'] == 42319417116])
# exit()

table = []

for st in unique_stream:
	st_df = stream.loc[stream['stream_id'] == st]
	st_np = st_df.to_numpy()
	st_increment = [0]
	for i in range (1, len(st_np)):
		st_increment.append(st_np[i][7])
	# print(st_increment)
	table.append(st_increment)

max_hours = max([len(i) for i in table])

total_followers = [0 for i in range (max_hours)]
frequency = [0 for i in range (max_hours)]

for line in table:
	for j in range(len(line)):
		total_followers[j] += line[j]
		frequency[j] += 1

y = [total_followers[i] / frequency[i] for i in range(max_hours)]
x = [i * 0.5 for i in range(max_hours)]

import matplotlib.pyplot as plt 
  
# This will plot a simple line chart
# with elements of x as x axis and y
# as y axis
plt.plot(x, y)
  
plt.title("Distribution of Viewers during the Stream")

# Adding the legends
plt.xlabel('hours into the stream')
plt.ylabel('viewers')
  
plt.show()
