import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = 'https://myanimelist.net/topanime.php?type=upcoming'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('a',{"class": "hoverinfo_trigger fl-l fs14 fw-b"})
i=1
for tag in tags:
    print(i,tag.contents[0])
    i += 1