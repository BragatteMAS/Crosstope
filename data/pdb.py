#pdb.py
#Ref.:https://www.youtube.com/watch?v=MjwWzBiAMck / refactor by Bragatte

import requests, os, bs4
from requests import get

domain = "http://www.crosstope.com"
#define separated html page dir
page = requests.get("http://www.crosstope.com/uploads/Complexos/")
#list all elements in the page select
html = page.text
soup = BeautifulSoup(html, "html.parser")

#function get every link in the page as element "a" in href
for link in soup.find_all('a'):
    url = link.get('href')
    #in this line change for the extension needed
    if ".pdb" in url:
        print(url)
        file_name = url.split('Complexos/',1)[1]
        with open(file_name, "wb") as file:
            response = get(domain + url)
            file.write(response.content)