import twitch, datetime
from datetime import timezone

#client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
#oath_token = 'nv8v0sdhbaebvqj6dcez1iy14nvogw'

client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
oath_token = 'rfah7wcdu2i7ptkgzjpe9gj2or1j8d'

client = twitch.TwitchHelix(client_id=client_id, oauth_token=oath_token)

user_file = open('data.txt', 'r')
user_data = user_file.readlines()
user_file.close()
num = 2100

stream_file = open('stream_week1.txt','a+')
inactive_file = open('inactive_week1.txt', 'a+')

for i in range(num):
	user_data[i] = user_data[i].replace('\n','')

for i in range (2101, 2101 + num):
	try:
			stream = client.get_streams(user_ids=user_data[i])
			user_follow = client.get_user_follows(to_id=user_data[i]).total
			current_time = datetime.datetime.utcnow()

			if len(stream) > 0:
				stream_id = stream[0]['id']
				stream_start = stream[0]['started_at']
				stream_game = stream[0]['game_name']
				stream_gameid = stream[0]['game_id']
				stream_lang = stream[0]['language']
				stream_viewer = stream[0]['viewer_count']
				dt = datetime.datetime.now()

				stream_file.write(stream_id + ',' + user_data[i] + ',' + str(stream_start) + ',' + stream_game + ',' + stream_gameid 
					+ ',' + stream_lang + ',' + str(stream_viewer) + ',' + str(user_follow) + ',' + str(current_time) + '\n')
			else:
				inactive_file.write(user_data[i] + ',' + str(user_follow) + ',' + str(current_time) + '\n')
			print(datetime.datetime.now())
		except requests.exceptions.HTTPError:
			continue
	except twitch.exceptions.TwitchNotProvidedException:
		continue

