#####################################################################
#Async Programming!
import os
import aiohttp
import aiofiles
import asyncio
from requests.exceptions import URLRequired

try:
    os.mkdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc')
except FileExistsError as e:
    print('The file path already exists!')

os.chdir('/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc')

crosstope = 'http://www.crosstope.com/uploads/Imagens_GRASP/V5/'
path = "[/home/bragatte/Documentos/GitHub/Crosstope/all_images/all_images_asnyc_event_loopc]"
included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
file_names = [fn for fn in os.listdir(path)
              if any(fn.endswith(ext) for ext in included_extensions)]

async with aiohttp.ClientSession() as session:
     async with session.get(crosstope) as resp:
        # 1. Capturing the image file name like we did before:
        crosstope_name = crosstope.endswith('jpg')[-1]
        # 2. Only proceed further if the HTTP response is 200 (Ok)
        if resp.status == 200:
            async with aiofiles.open(crosstope_name, mode='wb') as f:
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
            tasks.append(await fetch(session, URLRequired))
    data = await asyncio.gather(*tasks)
main(all_images)