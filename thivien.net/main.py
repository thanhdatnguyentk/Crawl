from bs4 import BeautifulSoup
import requests
import time
import json

URL = 'https://www.thivien.net/T%E1%BB%91-H%E1%BB%AFu/author-6uN9el0F61csLvlqLVN6gw'
INDEX = 0
file_content = "thivien.net\content.txt"
file_path = "DCS VietNam\output.json"
 
def get_item():
    global DATA
    html_text = requests.get(URL).text
    
    soup = BeautifulSoup(html_text, 'lxml')
    print(soup)
    items = soup.find_all('div', class_="poem-group-list")
    a = 0
    DATA = {}
    for idx,item in enumerate(items):
        urls = item.find_all('a', href = True)
        for poem_url in urls:
            url = URL + poem_url
            poem_text = requests.get(url).text
            pome_soup = BeautifulSoup(poem_text, 'lxml')

            title = pome_soup.find('h1').text
            poem_contents = pome_soup.find_all('br')
            for content in poem_contents:
                s = content.text
                with open(file_content, "a", encoding='utf-8') as f:
                    f.write(s)
            if title != None:
                a += 1
                print(f"{idx + INDEX}:")
                print(f"title: {title['title'].strip()}")
                with open(file_content, "r", encoding='utf-8') as file_obj:
                    s = file_obj.read()
                print(f"content: {s.strip()}")
                print(f"url: {url.strip()}")
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
    get_item()
    a,data = get_item()
    output.update(data)
    json_data = json.dumps(output,indent=4, ensure_ascii=False)
    with open(file_path, "w", encoding='utf-8') as json_file:
        json_file.write(json_data)

