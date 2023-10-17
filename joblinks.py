from bs4 import BeautifulSoup
import requests

url = 'https://www.dice.com/'  
response = requests.get(url)
links=[]

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    # Finding all <p> tags with class "seo-list-item"
    seo_list_items = soup.find_all('p', class_='seo-list-item')
    
    for item in seo_list_items:
        # Finds <a> tag 
        anchor_tags = item.find('a')
        # Gets the href from the <a> tag
        href = anchor_tags.get('href')
        # Appends in the array
        links.append(href)
            
else:
    print(f'Error: {response.status_code}')
print(links[48:])
print(len(links))