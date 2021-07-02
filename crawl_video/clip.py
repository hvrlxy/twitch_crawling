import twitch, datetime
from datetime import timezone
import numpy as np 
import pandas as pd

client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
oath_token = 'p6cb191gmvlaznd5n631g116gm087w'

#client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
#oath_token = 'z5fqe099m0ouc4xrpkf04vc2tyeqvw'

client = twitch.TwitchHelix(client_id=client_id, oauth_token=oath_token)

df = pd.read_csv('../data/stream_week1.csv')
df = pd.DataFrame(df)

mapping = {df.columns[0]: 'stream_id',
           df.columns[1]: 'user_id', df.columns[2]: 'start_time',
           df.columns[3]: 'game_name', df.columns[4]: 'game_id',
           df.columns[5]: 'language', df.columns[6]: 'viewer',
           df.columns[7]: 'followers',
           df.columns[8]:'current_time'}

df = df.rename(columns=mapping)
df['current_time'] = pd.to_datetime(df['current_time'])
df = df.loc[df['current_time'] < datetime.datetime(2021,6,17)]

unique_user = df['user_id'].unique()
clip_file = open('clip.csv', 'a+')

for user in unique_user:
	clips = client.get_clips(broadcaster_id=user, page_size=100)
	for clip in clips:
		created_at = clip['created_at']
		try:
			if created_at > datetime.datetime(2021,6,10) and created_at < datetime.datetime(2021,6,17):
				clip_id = clip['id']
				video_id = clip['video_id']
				broadcaster_id = clip['broadcaster_id']
				game_id = clip['game_id']
				title = clip['title'].replace(',','').replace('\n','')
				view_count = clip['view_count']
				language = clip['language']
				duration = clip['duration']

				clip_file.write(str(clip_id) + ',' + str(video_id) + ',' + str(broadcaster_id) + ',' 
					+ str(game_id) + ',' + title + ',' +
					str(view_count) + ',' + language + ',' + str(duration) + ',' + str(created_at) + '\n')
		except TypeError:
			continue

