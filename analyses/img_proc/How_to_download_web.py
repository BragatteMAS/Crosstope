# Download database from Crosstope
# REFactor @Bragatte 

from os import link
import requests, os
#from os import link
from bs4 import BeautifulSoup 

def get_images_link():
    #create response object
    r = requests.get(url)
    #create soup object
    soup = BeautifulSoup(r.content,'html5lib')
    #find all links on web-page
    links = soup.findAll('a') 
    # filter the link sending with .jpg 
    image_links = [url + link['href'] for link in links if link['href'].endswith('jpg')] #or pdb 

    return image_links
print(link)

def download_image_links(url):
    for link in image_links:
        '''iterate through all links in image_links 
        and download them one by one'''
        # obtain filename by splitting BASE_URL and getting last string =[-1]
        file_name = os.path.join(link.split('/')[-1])  
  
        #print("Downloading file:%s"%file_name)
          
        # create response object 
        #r = requests.get(url) #list urls
        r = requests.get(link, stream = True) #list names
            #check possible errors
        #if r.status_code == requests.codes.ok:
            #open file in the adress w=write b=binary & the name to close & download started 
        with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
        #print(f"Download finished: %s"%file_name)
        #else: #else show error
        #    r.raise_for_status()
  
    print ("All link from images downloaded!")
    return
 
if __name__ == "__main__":
    #BASE_URL
    url= 'http://www.crosstope.com/uploads/Imagens_GRASP/V5/' #img 
    #url = 'http://www.crosstope.com/uploads/Complexos/' #pdb
    OUTPUT_DIR = 'all_images'

    # getting all image links 
    image_links = get_images_link()
    # download all images 
    download_image_links(image_links)