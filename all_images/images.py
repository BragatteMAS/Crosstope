import requests, os
from bs4 import BeautifulSoup
import tldextract

os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images') 

url = ['http://www.crosstope.com/uploads/Imagens_GRASP/V5/','http://www.crosstope.com/uploads/Imagens_GRASP/V10/']

path = 'asnyc' #need this folder


# list to store any broken image URLs that didn’t return a 200 status code
broken_images = []

for page in url:
    domain_name = tldextract.extract(page).registered_domain


for page in url:
    #Extract domain name
    domain_name = tldextract.extract(page).registered_domain
    print(f"The domain name: {domain_name}")  

def download_file(url, adress):
    #request to server
    answer = requests.get(url,allow_redirects=True)

    if answer.status_code == requests.codes.ok:
        #open file in the adress w=write b=binary & the name to close
        with open(adress, 'wb') as new_file:
            #write in the download the content
            new_file.write(answer.content)
        print(f"Download finished. Save in: {adress}")
    else: #else show error
        answer.raise_for_status()


if __name__ == "__main__":
    for page in url:
            name_file = (f'{i}.jpg')
            #name_file = os.path.join(path, f'{i}.jpg')
            download_file(url.format(i),name_file)