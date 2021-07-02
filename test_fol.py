import twitch, datetime
from datetime import timezone

client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
oath_token = 'p6cb191gmvlaznd5n631g116gm087w'

#client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'
#oath_token = 'z5fqe099m0ouc4xrpkf04vc2tyeqvw'

client = twitch.TwitchHelix(client_id=client_id, oauth_token=oath_token)

alist = client.get_user_follows(to_id=71092938, page_size=100)
print(alist.total)

for user in alist:
	print(user['from_id'])