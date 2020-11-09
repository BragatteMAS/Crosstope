#!/usr/bin/
#Script de automação para baixar múltiplas imagens do Crosstope
#!pip install requests
import os       #paths to work at diff operational systems
import requests #connection with url files
 
def download_file(url, adress):
    #request to server
    answer = requests.get(url)
    #check possible errors
    if answer.status_code == requests.codes.ok:
        #open file in the adress w=write b=binary & the name to close
        with open(adress, 'wb') as new_file:
            #write in the download the content
            new_file.write(answer.content)
        print(f"Download finished. Save in: {adress}")
    else: #else show error
        answer.raise_for_status()
#action code
if __name__== "__main__": #(url, name)
    #inside {} should be the variable part from url database
    BASE_URL = 'http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0001_V5.jpg&fileName=A0201_0001_V5.jpg'
    #create a variable for outputs
    OUTPUT_DIR = 'output'
    #iteration for to multiple files
    for i in range(1,2):#start,stop
        #generate files as outputs.jpg
        file_name = os.path.join(OUTPUT_DIR,'0201_{}.jpg'.format(i))
        download_file(BASE_URL.format(i),file_name)

'''
payload = {file:, fileName:}
base_url = request.post('http://www.crosstope.com/download', data= payload)

http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0001_V5.jpg&fileName=A0201_0001_V5.jpg

http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0002_V5.jpg&fileName=A0201_0002_V5.jpg

http://www.crosstope.com/download?file=Imagens_GRASP\V5\H2DB_0190_V5.jpg&fileName=H2DB_0190_V5.jpg

Ref code tutorials:
https://www.youtube.com/watch?v=qx2LGtKzjxk&feature=em-uploademail
https://www.youtube.com/watch?v=tb8gHvYlCFshttps://www.youtube.com/results?search_query=requests+python+multiple+downloads
'''