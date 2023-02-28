from config import *
if server_url == "":
    server_url = input("Server url: ")
    server_port = input("Server port: ")
with open("config.py", "w") as f:
    f.write(f"""
server_url = "{server_url}"
server_port = "{server_port}"
server_url += ":""""")
    
from crontab import CronTab
my_cron = CronTab(user='root')
job = my_cron.new(command='python3 /client.py')
job.minute.every(1)
my_cron.write()
