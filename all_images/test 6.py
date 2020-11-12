#test 6

import re
import requests
from bs4 import BeautifulSoup
import os

site = 'http://pixabay.com'
directory = "pixabay/" #Relative to script location

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

for url in urls:
    #print(url)
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)

    with open(os.path.join(directory, filename.group(1)), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)