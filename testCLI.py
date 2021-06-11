# this program will run the crawling process for 2 hours, kill the process and run it again
import subprocess

try:
    while(True):
        print()
        print("Process Begain")
        subprocess.run('python3 user_data.py', shell=True)
        subprocess.run('python3 user_data.py', shell=True)
        subprocess.run('python3 user_data.py', shell=True)
        subprocess.run('python3 user_data.py', shell=True)
        subprocess.run('python3 crawl2.py', shell=True)
        subprocess.run('python3 crawl2.py', shell=True)
        subprocess.run('python3 crawl2.py', shell=True)
        subprocess.run('python3 crawl2.py', shell=True)
        

except KeyboardInterrupt:
       print("Keyboard Interrupt!")

