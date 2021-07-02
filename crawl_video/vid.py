import twitch, datetime
from datetime import timezone
import numpy as np 
import pandas as pd

client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
oath_token = 'p6cb191gmvlaznd5n631g116gm087w'

#client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
#oath_token = 'z5fqe099m0ouc4xrpkf04vc2tyeqvw'

client = twitch.TwitchHelix(client_id=client_id, oauth_token=oath_token)

df = pd.read_csv('../data/stream_week2+.csv')
df = pd.DataFrame(df)

mapping = {df.columns[0]: 'stream_id',
           df.columns[1]: 'user_id', df.columns[2]: 'start_time',
           df.columns[3]: 'game_name', df.columns[4]: 'game_id',
           df.columns[5]: 'language', df.columns[6]: 'viewer',
           df.columns[7]: 'followers',
           df.columns[8]:'current_time'}

df = df.rename(columns=mapping)
df['current_time'] = pd.to_datetime(df['current_time'])
unique_user = df['user_id'].unique()
vid_file = open('vid.csv', 'a+')

for user in unique_user:
	vids = client.get_videos(user_id=int(user), period='month', page_size=100,sort='time')
	for vid in vids:
		published_at = vid['published_at']
		try:
			if published_at >= datetime.datetime(2021,6,22) and published_at <= datetime.datetime(2021,6,29):
				vid_id = vid['id']
				stream_id = vid['stream_id']
				user_id = vid['user_id']
				title = vid['title'].replace(',','').replace('\n','')
				description = vid['description'].replace(',','').replace('\n','')
				view_count = vid['view_count']
				language = vid['language']
				vid_type = vid['type']
				duration = vid['duration']

				vid_file.write(str(vid_id) + ',' + str(stream_id) + ',' + str(user_id) + ',' + title + ',' +
					description + ',' + str(view_count) + ',' + language + ',' + vid_type + 
					',' + str(duration) + ',' + str(published_at) + '\n')
		except TypeError, ValueError:
			continue

