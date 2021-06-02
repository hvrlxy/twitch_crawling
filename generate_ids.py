# this program will generate 10000 twitch user IDs
import twitch

client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
oath_token = 'nv8v0sdhbaebvqj6dcez1iy14nvogw'

client = twitch.TwitchHelix(client_id=client_id, oauth_token=oath_token)
streams = client.get_streams()

user_list = []
for stream in streams:
	user_list.append(stream['user_id'])
	print(stream['user_id'])
	if len(user_list) > 10000:
		break
