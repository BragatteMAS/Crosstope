#Ref:https://sempioneer.com//python-for-seo/how-to-download-images-in-python/
#   = coments
##  = alternative code format
#####################################################################
#Python Imports

#!pip install tldextract

from urllib.request import urlretrieve
import requests
import os
import subprocess
import urllib.request
from bs4 import BeautifulSoup
import tldextract

#!mkdir all_images

os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images')  #same as cd all_images in term

#####################################################################
#Approach 1 - Images from PY list
# list to store any broken image URLs that didn’t return a 200 status code
broken_images = []

#image_urls =['https://understandingdata.com/']
#image_urls =['http://www.crosstope.com/uploads/Imagens_GRASP/V5/A0201_0001_V5.jpg','http://www.crosstope.com/uploads/Imagens_GRASP/V5/A0201_0108_V5.jpg']

for img in image_urls:
    # Files split  based upon / and extract the last split within [-1]
    file_name = img.split('/')[-1]
    #file_name = img.endswith('end=jpg')
    print(f"This is the file name: {file_name}")
    #print(img)
    # Now let's send a request to the image URL:
    r = requests.get(img, stream=True)
    # We can check that the status code is 200 before doing anything else:
    if r.status_code == 200:
        # This command below will allow us to write the data to a file as binary:
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    else:
        # We will write all of the images back to the broken_images list:
        broken_images.append(img)
#####################################################################
#Approach 2 - Download Multiple Images From Many HTML Web Pages

#webpages =['https://understandingdata.com/','https://understandingdata.com/data-engineering-services/',             'https://www.internetingishard.com/html-and-css/links-and-images/']
webpages = ['http://www.crosstope.com/uploads/Imagens_GRASP/V5/','http://www.crosstope.com/uploads/Imagens_GRASP/V10/','http://www.crosstope.com/uploads/Complexos/','http://www.crosstope.com']

for page in webpages:
    domain_name = tldextract.extract(page).registered_domain

url_dict = {}

for page in webpages:
    #Extract domain name
    domain_name = tldextract.extract(page).registered_domain
    print(f"The domain name: {domain_name}")  
    #acess webpage):
    r = requests.get(page)
    #check error
    if r.status_code == 200:
        #Create a URL dictionary
        url_dict[page] = []
        #webscrapping <img>tags BeautifulSoup / parse all content html
        soup = BeautifulSoup(r.content, 'html.parser')
        #Create a list all the <img> tag in the pageElements
        images = soup.findAll('img')
        #extend to avoid list of list (url_dict + images) 
        url_dict[page].extend(images)
    else:
        print('failed!')
            
#check if page has at least one image
for key, value in url_dict.items():
    ##print(key) #complete url
    ##print(value) #links
    #print just the page with content
    if len(value) > 0:
        print(f"This domain: {key} has more than 1 image on the web page.")
#pythonic way
cleaned_dict = {key: value for key, value in url_dict.items() if len(value) > 0}

#Separate relative and absolute path
#cleaning URLs
for key, images in cleaned_dict.items():
    #check if have list types
    ##print(type(value))
    for image in images:
        #attrs=attributes in list
        print(image.attrs['src'])

#Removing // add URL
all_images = []

for key, images in cleaned_dict.items():
    #create clean_url and domain for every page
    clean_urls = []
    domain_name = tldextract.extract(key).registered_domain
    #Looping over every image per url
    for image in images:
        #list source(src) attributes (attrs) from images
        source_image_url = image.attrs['src']
        #clean data
        if source_image_url.startswith("//"):
            pass
        elif domain_name not in source_image_url and 'http' not in source_image_url:
            url = "https://" + domain_name + source_image_url
            all_images.append(url)
        else:
            all_images.append(source_image_url)

print(all_images[0:5])

#Download for pc
def extract_images(image_urls_list:list, directory_path):
    # Changing directory into a specific folder:
    os.chdir(directory_path)
    # Downloading all of the images
    for img in image_urls_list:
        file_name = img.split('/')[-1]
        #loop [https:// and https://www.]
        url_paths_to_try = [img, img.replace('https://', 'https://:www.')]
        for url_image_path in url_paths_to_try:
            print(url_image_path)
            try:
                r = requests.get(img, stream=True)
                if r.status_code == 200:
                    with open(file_name, 'wb') as f:
                        for chunck in r:
                            f.write(chunck)
            except Exception as e:
                pass

path ='/home/bragatte/Documentos/GitHub/Crosstope/all_images'

extract_images(image_urls_list=all_images, directory_path=path)

#####################################################################
#How To Speed Up Your Image Downloads
def extract_single_image(img):
    file_name = img.split('/')[-1]

    # Let's try both of these versions in a loop [https:// and https://www.]
    url_paths_to_try = [img, img.replace('https://', 'https://www.')]
    for url_image_path in url_paths_to_try:
        try:
            r = requests.get(img, stream=True)
            if r.status_code == 200:
                with open(file_name, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
            return "Completed"
        except Exception as e:
            return "Failed"
all_images[0:5]

try:
    os.mkdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/asnyc')
except FileExistsError as e:
    print('The file path already exists!')

os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/asnyc')

import concurrent.futures
import urllib.request

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(extract_single_image, image_url) for image_url in all_images}
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            url = future_to_url[future]
        except Exception as e:
            pass
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))

#####################################################################
#Async Programming!
#!pip install aiohttp
#!pip install aiofiles

import aiohttp
import aiofiles
import asyncio

try:
    os.mkdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc')
except FileExistsError as e:
    print('The file path already exists!')

os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc')

#How To Download 1 File Asychronously
print(all_images[0:1])
#Single image
single_image = 'https://understandingdata.com/wp-content/uploads/2019/09/james-anthony-phoenix.jpg'
async with aiohttp.ClientSession() as session:
     async with session.get(single_image) as resp:
        # 1. Capturing the image file name like we did before:
        single_image_name = single_image.split('/')[-1]
        # 2. Only proceed further if the HTTP response is 200 (Ok)
        if resp.status == 200:
            async with aiofiles.open(single_image_name, mode='wb') as f:
                await f.write(await resp.read())
                await f.close()
# Multiple images
async def fetch(session, url):
    async with session.get(url) as resp:
        # 1. Capturing the image file name like we did before:
        url_name = url.split('/')[-1]
        # 2. Only proceed further if the HTTP response is 200 (Ok)
        if resp.status == 200:
            async with aiofiles.open(url_name, mode='wb') as f:
                await f.write(await resp.read())
                await f.close()

async def main(image_urls:list):
    tasks = []
    headers = {
        "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    async with aiohttp.ClientSession(headers=headers) as session:
        for image in image_urls:
            tasks.append(await fetch(session, url))
    data = await asyncio.gather(*tasks)
main(all_images)

#####################################################################
#How To Download Multiple Python Files Inside Of A Python File (.py)
with open('images.txt', 'w') as f:
    for item in all_images:
        f.write(f"{item}n")
#Create A Python File
# Package / Module Imports
import aiohttp
import aiofiles
import asyncio
import os

# 1. Choose A Path - You will need to change this to your desired directory:
path = '/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc'

try:
    os.mkdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc')
except FileExistsError as e:
    print('The file path already exists!')

# 2. Changing directory into that specific path:
os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc')

# 3. Reading the URLs from the text file:
with open('images.txt', 'r') as f:
    image_urls = f.read().split('n')

# 2. Creating the async functions:
async def fetch(session, url):
    async with session.get(url) as resp:
        # 1. Capturing the image file name like we did before:
        url_name = url.split('/')[-1]
        # 2. Only proceed further if the HTTP response is 200 (Ok)
        if resp.status == 200:
            async with aiofiles.open(url_name, mode='wb') as f:
                await f.write(await resp.read())
                await f.close()

async def main(image_urls:list):
    tasks = []
    headers = {
        "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    async with aiohttp.ClientSession(headers=headers) as session:
        for image in image_urls:
            tasks.append(await fetch(session, image))
    data = await asyncio.gather(*tasks)

# 3. Executing all of the asyncio tasks:
try:
    asyncio.run(main(image_urls))
except Exception as e:
    print(e)