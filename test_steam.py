import requests
import json

# preprocessing, put it in the beginning of the user_data.py file
appid = open('appid.txt', 'r') # need to download the appid.txt file first

appid = appid.readlines()

appid_dict = {}

for line in appid:
	split_line = line.replace('\n','').split(' ; ')
	appid_dict[split_line[1]] = split_line[0]

#this function takes the name of the game return by Twitch, and search for the current number
#of players on steam of that game. If the game is not in steam, it return None
def get_steam_player(game_name: str):
	if game_name not in appid_dict:
		return None
	test_id = appid_dict[game_name]

	x = requests.get('https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=' + test_id)

	for a in x:
		continue

	y = json.loads(a)

	if y['response']['result'] == 0:
		return None 
	else:
		return y['response']['player_count']

print(get_steam_player('Grand Theft Auto V'))
print(get_steam_player('saindscd'))

