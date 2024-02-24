from selenium import webdriver
import json
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import requests
import queue
from selenium.webdriver.chrome.options import Options

q = queue.Queue()

value_proxies = []

with open("thivien.net/valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

file_path = "thivien.net\output.json"

global DATA

website = 'https://www.thivien.net/T%E1%BB%91-H%E1%BB%AFu/author-6uN9el0F61csLvlqLVN6gw'

driver = webdriver.Chrome()

driver.get(website)
all_matches_list = driver.find_elements("xpath",'//div[@class="poem-group-list"]//a')
links = []
for link in all_matches_list:

  
    url = link.get_attribute('href')
    links.append(url)

with open(file_path, "w", encoding='utf-8') as json_file:
        json_file.write("")
for idx, link in enumerate(links):
    stt = idx
    driver.get(link)
    title = driver.find_element("xpath", '//h1').text
    content = driver.find_element("xpath", '//div[@class="poem-content"]//p').text
    print(f"{stt} :")
    print(f"       {title}")
    print(f"       {content}")
    print(f"       {link}")
    data = {
                        stt:
                        {
                            "title": title.strip(),
                            "contetn": content.strip(),
                            "url": link.strip()
                        }
                }
    json_data = json.dumps(data,indent=4, ensure_ascii=False)
    with open(file_path, "a", encoding='utf-8') as json_file:
        json_file.write(json_data)
    
    proxy_ip_port = q.get()
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port
    
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server={}'.format(proxy.http_proxy))

    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(2)




    