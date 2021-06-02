# this program go through the list of 10000 user ids, grasp every stream currently occur
# and write it down in the stream_data.txt
import twitch

client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
oath_token = 'nv8v0sdhbaebvqj6dcez1iy14nvogw'

client = twitch.TwitchHelix(client_id=client_id, oauth_token=oath_token)

user_file = open('data.txt', 'r')
user_data = user_file.readlines()
user_file.close()
num = len(user_data)

stream_file = open('stream_data.txt','a+')

for i in range(num):
	user_data[i] = user_data[i].replace('\n','')

i = 0
while(True):
	# since the api only let us get stream info from 20 users at a time, we increment 
	# i by 20 at a time
	streams = client.get_streams(user_ids=user_data[i:i+20])
	for stream in streams:
		user = stream['user_id']
		stream_start = stream['started_at']
		stream_game = stream['game_name']
		stream_gameid = stream['game_id']
		stream_lang = stream['language']
		stream_viewer = stream['viewer_count']
		user_followers = client.get_user_follows(to_id=user)
		user_follow = user_followers.total

		stream_file.write(user + ',' + str(stream_start) + ',' + stream_game + ',' + stream_gameid 
			+ ',' + stream_lang + ',' + str(stream_viewer) + ',' + str(user_follow) + '\n')
	i = i + 20
	if i > 9999:
		i = 0

