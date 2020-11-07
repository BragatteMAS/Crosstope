#!/usr/bin/
#Script de automação para baixar múltiplas imagens do Crosstope
#!pip install requests
import os, requests

def download_file(url, adress):
    #request to server
    answer = requests.get(url)
    if answer.status_code == requests.codes.ok:
        #open file in the adress w=write b=binary & the name to close
        with open(adress, 'wb') as new_file:
            #write in the download the content
            new_file.write(answer.content)
        print(f"Download finished. Save in: {adress}")
    else:
        answer.raise_for_status()

if __name__== "__main__":
    download_file('http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0001_V5.jpg&fileName=A0201_0001_V5.jpg', '0201_1.jpg')

'''
#Alternative change only the variation into url
if __name__== "__main__":
    base_url = "https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf"
    output_dir = 'output'
    for i in range (1, 26):
        file_name = os.path.join(output_dir, f'Class_notes_{i}.pdf')
        download_file(base_url.format(i), file_name)

#http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0001_V5.jpg&fileName=A0201_0001_V5.jpg

#http://www.crosstope.com/download?file=Imagens_GRASP\V5\A0201_0002_V5.jpg&fileName=A0201_0002_V5.jpg

http://www.crosstope.com/download?file=Imagens_GRASP\V5\H2DB_0190_V5.jpg&fileName=H2DB_0190_V5.jpg
'''