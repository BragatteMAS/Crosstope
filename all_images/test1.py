#tests
import requests, os
 
def download_file(url, adress):
    #request to server
    answer = requests.get(url,allow_redirects=True)
    #check possible errors
    if answer.status_code == requests.codes.ok:
        #open file in the adress w=write b=binary & the name to close
        with open(adress, 'wb') as new_file:
            #write in the download the content
            new_file.write(answer.content)
        print(f"Download finished. Save in: {adress}")
    else: #else show error
        answer.raise_for_status()

if __name__ == "__main__":
    BASE_URL = 'http://www.crosstope.com/uploads/Imagens_GRASP/V5/{}.jpg'
    OUTPUT_DIR = 'asnyc' #need this folder
    for page in BASE_URL:
            name_file = os.path.join(OUTPUT_DIR, f'{page}.png')
            download_file(BASE_URL.format(page),name_file)
