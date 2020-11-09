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
    BASE_URL = 'http://www.crosstope.com/uploads/Imagens_GRASP/V5/A0201_000{}_V5.jpg'
    OUTPUT_DIR = 'output'
    for i in range(1,4):
            name_file = os.path.join(OUTPUT_DIR, f'crosstope_{i}.jpg')
            download_file(BASE_URL.format(i),name_file)
            

##############################
#'http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0001_V5.jpg&fileName=A0201_0001_V5.jpg'
#http://www.crosstope.com/uploads/Imagens_GRASP/V5/A0201_0001_V5.jpg
#http://www.crosstope.com/uploads/Imagens_GRASP/V5/A0201_0108_V5.jpg