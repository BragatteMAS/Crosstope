{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python38264bitdszcondaf5b1811fa9c743e9afd06fda34ac3218",
   "display_name": "Python 3.8.2 64-bit ('dsz': conda)"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests, os\n",
    "from bs4 import BeautifulSoup\n",
    "import tldextract"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = ['http://www.crosstope.com/uploads/Imagens_GRASP/V5/','http://www.crosstope.com/uploads/Imagens_GRASP/V10/']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "path = 'asnyc' #need this folder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "broken_images = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "for page in url:\n",
    "    domain_name = tldextract.extract(page).registered_domain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_dict = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "The domain name: crosstope.com\nThe domain name: crosstope.com\n"
     ]
    }
   ],
   "source": [
    "for page in url:\n",
    "    #Extract domain name\n",
    "    domain_name = tldextract.extract(page).registered_domain\n",
    "    print(f\"The domain name: {domain_name}\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def download_file(url, adress):\n",
    "    #request to server\n",
    "    answer = requests.get(url,allow_redirects=True)\n",
    "\n",
    "    if answer.status_code == requests.codes.ok:\n",
    "        #open file in the adress w=write b=binary & the name to close\n",
    "        with open(adress, 'wb') as new_file:\n",
    "            #write in the download the content\n",
    "            new_file.write(answer.content)\n",
    "        print(f\"Download finished. Save in: {adress}\")\n",
    "    else: #else show error\n",
    "        answer.raise_for_status()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "InvalidSchema",
     "evalue": "No connection adapters were found for \"['http://www.crosstope.com/uploads/Imagens_GRASP/V5/', 'http://www.crosstope.com/uploads/Imagens_GRASP/V10/']\"",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mInvalidSchema\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-14-3c5bb85134cf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m             \u001b[0mname_file\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34mf'{page}.jpg'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m             \u001b[0;31m#name_file = os.path.join(path, f'{i}.jpg')\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m             \u001b[0mdownload_file\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mname_file\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-11-3c910d67481e>\u001b[0m in \u001b[0;36mdownload_file\u001b[0;34m(url, adress)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mdownload_file\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0madress\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0;31m#request to server\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0manswer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mallow_redirects\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0manswer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus_code\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mrequests\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcodes\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mok\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/envs/dsz/lib/python3.8/site-packages/requests/api.py\u001b[0m in \u001b[0;36mget\u001b[0;34m(url, params, **kwargs)\u001b[0m\n\u001b[1;32m     74\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     75\u001b[0m     \u001b[0mkwargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetdefault\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'allow_redirects'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 76\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'get'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     77\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     78\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/envs/dsz/lib/python3.8/site-packages/requests/api.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(method, url, **kwargs)\u001b[0m\n\u001b[1;32m     59\u001b[0m     \u001b[0;31m# cases, and look like a memory leak in others.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m     \u001b[0;32mwith\u001b[0m \u001b[0msessions\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSession\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0msession\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 61\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     62\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     63\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/envs/dsz/lib/python3.8/site-packages/requests/sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[1;32m    528\u001b[0m         }\n\u001b[1;32m    529\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 530\u001b[0;31m         \u001b[0mresp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    531\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    532\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/envs/dsz/lib/python3.8/site-packages/requests/sessions.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, **kwargs)\u001b[0m\n\u001b[1;32m    635\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    636\u001b[0m         \u001b[0;31m# Get the appropriate adapter to use\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 637\u001b[0;31m         \u001b[0madapter\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_adapter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    638\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    639\u001b[0m         \u001b[0;31m# Start time (approximately) of the request\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/envs/dsz/lib/python3.8/site-packages/requests/sessions.py\u001b[0m in \u001b[0;36mget_adapter\u001b[0;34m(self, url)\u001b[0m\n\u001b[1;32m    728\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    729\u001b[0m         \u001b[0;31m# Nothing matches :-/\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 730\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mInvalidSchema\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"No connection adapters were found for {!r}\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    731\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    732\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mInvalidSchema\u001b[0m: No connection adapters were found for \"['http://www.crosstope.com/uploads/Imagens_GRASP/V5/', 'http://www.crosstope.com/uploads/Imagens_GRASP/V10/']\""
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    for page in url:\n",
    "            name_file = os.path.join(path, (f'{page}.jpg')\n",
    "            #name_file = os.path.join(path, f'{i}.jpg')\n",
    "            download_file(url,name_file)"
   ]
  }
 ]
}