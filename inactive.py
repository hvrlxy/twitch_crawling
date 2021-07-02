import pandas as pd
import numpy as np
import math

inactive = pd.read_csv('data/inactive_week1.csv')
inactive = pd.DataFrame(inactive)

users = inactive['user_id'].unique()
print(users)

for user in users:
	user_pd = inactive.loc[inactive['user_id'] == user]
	print(user_pd)
	exit()