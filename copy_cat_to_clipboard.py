import urllib.request as url_req
import json
from io import BytesIO
import win32clipboard as clip
from PIL import Image

def send_to_clipboard(clip_type, data):
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(clip_type, data)
    clip.CloseClipboard()

api_key = 'live_HfIv8G0DV3Drm1XBvFKucJmxlxq1GNRQ6U5XU28CeWKCMtnhQ4ZeaIzglJKChP2j'
image_request = url_req.Request('https://api.thecatapi.com/v1/images/search',headers={'x-api-key':api_key})
getRandomCat = json.loads(url_req.urlopen(image_request).read())[0]['url']
cat_request = url_req.Request(getRandomCat,headers={"User-Agent": "Mozilla/5.0"})
cat = url_req.urlopen(cat_request).read()
img = Image.open(BytesIO(cat))
output = BytesIO()
img.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()
send_to_clipboard(clip.CF_DIB, data)