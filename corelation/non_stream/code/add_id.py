import pandas as pd
import numpy as np
import math
import datetime

inactive = pd.read_csv('../../data/inactive_week1.csv')
inactive = pd.DataFrame(inactive)

mapping = {inactive.columns[0]: 'user_id',
           inactive.columns[1]: 'follower', 
           inactive.columns[2]: 'current_time'}

inactive_2 = pd.read_csv('../../data/inactive_week2+.csv')
inactive_2 = pd.DataFrame(inactive_2)
inactive_2 = inactive_2.rename(columns=mapping)
inactive = inactive.rename(columns=mapping)

inactive = inactive.append(inactive_2)


inactive['current_time'] = pd.to_datetime(inactive['current_time'])
print(inactive)

users = inactive['user_id'].unique()

index = [i for i in range(len(inactive))]
inactive['index'] = index

ids = [0 for i in range(len(inactive))]
id = 0
for user in users:
	user_pd = inactive.loc[inactive['user_id'] == user]
	st_np = user_pd.to_numpy()
	time_change = datetime.timedelta(minutes=40)
	ids[st_np[0, 3]] = id
	for i in range(1, len(st_np)):
		if st_np[i - 1,2] + time_change > st_np[i,2]:
			#print(st_np[i,3])
			ids[st_np[i,3]] = ids[st_np[i - 1,3]]
		else:
			id +=1
			ids[st_np[i,3]] = id

inactive['id'] = ids
inactive.to_csv(path_or_buf='new_inactive')
