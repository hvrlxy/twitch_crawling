import pandas as pd
import numpy as np
import math

vid = open('vid.csv', 'r')

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
unique_user = list(df['user_id'].unique())

vid_count = []

for user in unique_user:
	user_df = df.loc[df['user_id'] == user]
	vid_count.append(len(user_df))

mapping = {}
for i in vid_count:
    if i in mapping:
        mapping[i] += 1
    else:
        mapping[i] = 1

import matplotlib.pyplot as plt

x = list(mapping.keys())
y = [mapping[i] for i in x]

# x = [math.log10(max(1,float(i))) for i in x]
# y = [math.log10(float(i)) for i in y]

# This will plot a simple scatter chart
plt.bar(x, y)

#name the axis
plt.xlabel('# of videos per users')
plt.ylabel('# frequency')
  
# Title to the plot
plt.title("Number of Videos Per User Per Week")
  
plt.show()


