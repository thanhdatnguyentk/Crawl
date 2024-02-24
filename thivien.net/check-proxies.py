import threading
import queue
import requests

q = queue.Queue()

value_proxies = []

with open("thivien.net\proxy-list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("https://www.thivien.net/",
                               proxies={"http": proxy, "https:": proxy})
        except: 
            continue
        if res.status_code == 200:
            print(proxy)    

for _ in range(10):
    threading.Thread(target=check_proxies).start()