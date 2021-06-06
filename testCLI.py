# this program will run the crawling process for 2 hours, kill the process and run it again
import os, signal

for i in range (48):
    process = os.system('gtimeout 1800 python3 user_data.py')
#    print('end one round')
# os.kill(process, signal.SIGKILL)
