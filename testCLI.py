# this program will run the crawling process for 2 hours, kill the process and run it again
import os, signal

for i in range (12):
    process = os.system('gtimeout 7200 python3 user_data.py > stream_data.txt')
#    print('end one round')
# os.kill(process, signal.SIGKILL)
