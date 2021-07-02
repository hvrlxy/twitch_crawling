import pandas as pd
import numpy as np
import math

import datetime

inactive = pd.read_csv('new_inactive.csv')
inactive = inactive.drop(columns=['index', 'Unnamed: 0'])

unique_inactive = inactive['id'].unique()

table = []
for ia in unique_inactive:
	ia_pd = inactive.loc[inactive['id'] == ia]
	ia_np = ia_pd.to_numpy()
	if len(ia_np) > 1:
		incr = [0]
		for i in range(1,len(ia_np)):
			try:
				val = int(ia_np[i,1] - ia_np[i - 1, 1])
				incr.append(val)
			except ValueError:
				break

		table.append(incr)

max_hours = max([len(i) for i in table])

total_followers = [0 for i in range (max_hours)]
frequency = [0 for i in range (max_hours)]

for line in table:
	for j in range(len(line)):
		total_followers[j] += line[j]
		frequency[j] += 1

y = [total_followers[i] / frequency[i] for i in range(max_hours)]
x = [i * 0.5 for i in range(max_hours)]

import matplotlib.pyplot as plt 
  
# This will plot a simple line chart
# with elements of x as x axis and y
# as y axis
plt.plot(x, y)
  
plt.title("Distribution of Followers gained during an Inactive Period")

# Adding the legends
plt.xlabel('hours into the inactive period')
plt.ylabel('followers gained')
  
plt.show()


