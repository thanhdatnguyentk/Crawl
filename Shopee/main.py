from selenium import webdriver
import json
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import requests
import queue
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# q = queue.Queue()

# value_proxies = []

# with open("thivien.net/valid_proxies.txt", "r") as f:
#     proxies = f.read().split("\n")
#     for p in proxies:
#         q.put(p)
global DATA

file_path = "Shopee\output.json"

username = "ngthanhdat1303"
password = "Dat13031977"

driver = webdriver.Chrome()

website = 'https://shopee.vn/buyer/login?from=https%3A%2F%2Fshopee.vn%2Fuser%2Faccount%2Fprofile&next=https%3A%2F%2Fshopee.vn%2Fuser%2Faccount%2Fprofile'
driver.get(website)

driver.find_element("xpath", '//input[@name="loginKey"]').send_keys(username)
time.sleep(2)
driver.find_element("xpath", '//input[@name="password"]').send_keys(password)   
time.sleep(2)
driver.find_element("xpath", '//button[contains(text(), "Đăng nhập")]').click()
time.sleep(20)

website = 'https://shopee.vn/apple_flagship_store?page=0&shopCollection=124474144'

driver.get(website)

time.sleep(10)

all_matches_list = driver.find_elements("xpath",'//div[@class="shop-collection-view__item col-xs-2-4"]//a')
links = []
for link in all_matches_list:
    url = link.get_attribute('href')
    links.append(url)

print(len(links))
time.sleep(10)

# with open(file_path, "w", encoding='utf-8') as json_file:
#         json_file.write("")
# for idx, link in enumerate(links):
#     stt = idx
#     driver.get(link)
#     title = driver.find_element("xpath", '//h1').text
#     content = driver.find_element("xpath", '//div[@class="poem-content"]//p').text
#     print(f"{stt} :")
#     print(f"       {title}")
#     print(f"       {content}")
#     print(f"       {link}")
#     data = {
#                         stt:
#                         {
#                             "title": title.strip(),
#                             "contetn": content.strip(),
#                             "url": link.strip()
#                         }
#                 }
#     json_data = json.dumps(data,indent=4, ensure_ascii=False)
#     with open(file_path, "a", encoding='utf-8') as json_file:
#         json_file.write(json_data)
    
#     # proxy_ip_port = q.get()
#     # proxy = Proxy()
#     # proxy.proxy_type = ProxyType.MANUAL
#     # proxy.http_proxy = proxy_ip_port
#     # proxy.ssl_proxy = proxy_ip_port
    
#     # chrome_options = Options()
#     # chrome_options.add_argument('--proxy-server={}'.format(proxy.http_proxy))

#     # driver = webdriver.Chrome(options=chrome_options)
#     time.sleep(2)




    