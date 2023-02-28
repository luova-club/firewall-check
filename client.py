import requests
import json
import subprocess
from config import server_url, server_port
from classes import time_item, log_item
def read_log():
    logs = []
    count = 0
    logs_dict = {"logs": []}
    logs_dict_list = logs_dict["logs"]
    with open("/var/log/auth.log", "r") as f:
        for line in f.readlines():
            if not "Accepted" in line and not "Failed" in line and not "Invalid" in line:
                continue
            log = log_item(line)
            log.parse_log()
            log = log.make_json()
            logs.append(log)
    for log in logs:
        logs_dict_list.append(log)
    return logs_dict


response = requests.post(f"{server_url}{server_port}/upload", json=read_log())
print(response.text)
respon = response.json()
to_ban = []
subprocess.run(["iptables", "-F"])
for ip in respon["ban"]:
    print(f"Banning {ip}")
    
    subprocess.run(["iptables", "-I" "INPUT", "-s", ip, "-j", "DROP"])
subprocess.run(["iptables-save"])

