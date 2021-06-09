# this program will run the crawling process for 2 hours, kill the process and run it again
import subprocess

try:
    while(True):
        print()
        print("Process Begain")
        subprocess.run('gtimeout 1800 python3 user_data.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data2.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data2.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data2.py', shell=True)
        subprocess.run('gtimeout 1800 python3 user_data2.py', shell=True)
        

except KeyboardInterrupt:
       print("Keyboard Interrupt!")

