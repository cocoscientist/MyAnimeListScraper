import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

list1 = ['airing','upcoming','tv','movie','ova','ona','special','bypopularity','favorite']
url = 'https://myanimelist.net/topanime.php'
xz = 'a'

def inputFunc():
    global url
    xz = input('Enter the category you want: ')
    xz = xz.lower()
    if(xz=='all anime'):
        url=url
    elif(list1.count(xz)==1):
        url += '?type='+xz
    else:
        print("Incorrect parameter")
        inputFunc()

inputFunc()
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('a',{"class": "hoverinfo_trigger fl-l fs14 fw-b"})
i=1
for tag in tags:
    print(i,tag.contents[0])
    i += 1