from bs4 import BeautifulSoup
import requests
import time
import json

URL = 'https://vnexpress.net/phap-luat/ho-so-pha-an'
INDEX = 0
file_path = "vnexpress\output.json"
def load_next_page():
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    for i in soup.find_all('a', class_= 'next-page', href = True): 
        print(i['href']) 
        url = 'https://vnexpress.net' + i['href']
        break
    return url
 
def get_item():
    global DATA
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    items = soup.find_all('article', class_='item-news')
    a = 0
    DATA = {}
    for idx,item in enumerate(items):
        title = item.find('h2', class_='title-news')
       
        if title != None:
            a += 1
            title = item.find('h2', class_='title-news').text
            url = item.find('a', href = True)
            content_text = requests.get(url['href']).text
            content_soup = BeautifulSoup(content_text, 'lxml')
            contents = content_soup.find_all('p', class_='Normal')
            file_content = "vnexpress\content.txt"
            for content in contents:
                s = content.text
                with open(file_content, "a", encoding='utf-8') as f:
                    f.write(s)
            print(f"{idx + INDEX}:")
            print(f"title: {title.strip()}")
            with open(file_content, "r", encoding='utf-8') as file_obj:
                s = file_obj.read()
            print(f"content: {s.strip()}")
            print(f"url: {url['href'].strip()}")
            print("")
            with open(file_content, "w", encoding='utf-8') as file_obj:
                file_obj.write('')
            data = {
                        idx + INDEX:
                        {
                            "title": title.strip(),
                            "contetn": s.strip(),
                            "url": url['href'].strip()
                        }
                }
            index = idx + INDEX
            if (DATA == None):
                DATA = json.loads(data)
            else: 
                DATA.update(data)
    
    return a, DATA
   
if __name__== '__main__':
    output ={}
    while True:
        get_item()
        print(f'Wanna get more?')
        print(f'Y/N')
        x = input()
        a,data = get_item()
        if x == 'Y':
            URL = load_next_page()
            output.update(data)
            INDEX += a
        else:
            output.update(data)
            break
    json_data = json.dumps(output,indent=4, ensure_ascii=False)
    with open(file_path, "w", encoding='utf-8') as json_file:
        json_file.write(json_data)

