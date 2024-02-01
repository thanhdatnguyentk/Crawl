from bs4 import BeautifulSoup
import requests
import time
import json

URL = 'https://dangcongsan.vn/tu-tuong-van-hoa'
INDEX = 0
file_path = "DCS VietNam\output.json"
def load_next_page():
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    for i in soup.find_all('a', href = True): 
        url = 'https://dangcongsan.vn/tu-tuong-van-hoa' + i['href']
        break
    return url
 
def get_item():
    global DATA
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    items = soup.find_all('article')

    a = 0
    DATA = {}
    for idx,item in enumerate(items):
        title = item.find('div', class_='box-thumbnail')
       
        if title != None:
            a += 1
            title = item.find('a')
            description = item.find('p', class_='pctent').text
            url = item.find('a', href = True)
            print(f"{idx + INDEX}:")
            print(f"title: {title['title'].strip()}")
            print(f"description: {description.strip()}")
            print(f"url: {url['href'].strip()}")
            print("")
            data = {
                        idx + INDEX:
                        {
                            "title": title['title'].strip(),
                            "description": description.strip(),
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
        if x == 'Y':
            URL = load_next_page()
            a,data = get_item()
            output.update(data)
            INDEX += a
        else:
            a,data = get_item()
            output.update(data)
            break
    json_data = json.dumps(output,indent=4, ensure_ascii=False)
    with open(file_path, "w", encoding='utf-8') as json_file:
        json_file.write(json_data)

