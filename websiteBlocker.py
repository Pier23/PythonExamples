''' This script will block during a while of time any website defined
in 'website.txt', writing them on hosts file and doing a redirect at localhost 127.0.0.1  '''
import time
from datetime import datetime as dt

hosts_path_mac = "/etc/hosts"
hosts_path_win =r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"

website_list = open('website_list.txt', 'r')
website_list = [w.strip('\n') for w in website_list]


while True:
    #Set a while of time during the filter is active
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now()< dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours...')
        with open(hosts_temp, 'r+') as file: #Open host file in reading and writing
            content = file.read() #Reading
            for website in website_list:
                if website in content: #Check if the websites are already in hosts file
                    pass
                else:
                    file.write(redirect + " " + website + '\n') #writing the websites in hosts file
    else: # if we are not in the while
        with open(hosts_temp , 'r+') as file:
            content = file.readlines() #Reading the lines
            file.seek(0) #Set the coursor on top
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line) # Reset of hosts file to default and turn off the filter
            file.truncate()
        print('Free time...')
    time.sleep(5)
