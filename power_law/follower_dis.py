import matplotlib.pyplot as plt
import twitch

user_ids = open('mapping.txt', 'r')
user_ids = user_ids.readlines()
user_ids = [line.replace('\n', '').split(': ') for line in user_ids]

mapping = {}
import math 

for i in user_ids:
	new_i = math.floor(int(i[1]) / 5000) * 5000
	if new_i <= 0:
		continue
	if new_i not in mapping:
		mapping[new_i] = 1
	else:
		mapping[new_i] = mapping[new_i] + 1

x = list(mapping.keys())
y = [mapping[i] for i in x]

x = [math.log10(float(i)) for i in x]
y = [math.log10(float(i)) for i in y]

# This will plot a simple scatter chart
plt.scatter(x, y)

#name the axis
plt.xlabel('# of Followers')
plt.ylabel('# frequency')
  
# Title to the plot
plt.title("Distribution of Followers")
  
plt.show()