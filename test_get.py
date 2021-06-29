import requests

x = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')

applist = ''
for line in x:
	applist += (str(line).replace('\'b\'','').replace(']}}', '').replace('{"applist":{"apps":[', ''))

dict_list = applist.split('},{')

for d in dict_list:
	aline = d.replace('\'b\'','').replace('"appid":','').replace('b\'{','')
	aline = aline.split(',"name":"')
	print(aline[0] + ' ; ' + aline[1].replace("\"",'').replace('}\'',''))

