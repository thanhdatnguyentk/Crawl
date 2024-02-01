from bs4 import BeautifulSoup
import requests
import time
import json

URL = 'https://shopee.vn/apple_flagship_store?page=0&shopCollection=124474144'
INDEX = 0
file_path = "Shopee/output.json"

def load_next_page():
    return

def get_item():
    global DATA
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    items = soup.find_all('div', class_='shop-search-result-view')
    print(html_text)
    a = 0
    DATA = {}
    for item in items:
        item_url = item.find('a')
        product_name = item.text
        item_text = requests.get(item_url).text
        item_soup = BeautifulSoup(item_text, 'lxml')
        comments = item_soup.find_all('div', class_='shopee-product-rating')
        
        for idx,comment in enumerate(comments):
            comment_name = comment.find('a', class_='shopee-product-rating__author-name')
        
            if comment_name != None:
                a += 1
                name = comment.find('a', class_='shopee-product-rating__author-name').text
                description = comment.find('div', style_='position: relative; box-sizing: border-box; margin: 15px 0px; font-size: 14px; line-height: 20px; color: rgba(0, 0, 0, 0.87); word-break: break-word; white-space: pre-wrap;').text
                
                print(f"{idx + INDEX}:")
                print(f"product: {product_name.strip()}")
                print(f"description: {description.strip()}")
                print(f"name: {name.strip()}")
                print("")
                data = {
                            idx + INDEX:
                            {
                                "product": product_name.strip(),
                                "description": description.strip(),
                                "name": name.strip()
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

