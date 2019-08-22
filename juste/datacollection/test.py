
from manager import TorPoolManager
from lxml import html,etree
import requests
import time

url = "https://foursquare.com/v/"

pool = TorPoolManager()
pool.switchPort(True)

venues = open('venues.csv','r').readlines()

s = requests.Session()

headers= {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
'Connection': 'keep-alive',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br'
}

#for i in range(1,len(venues)):
for i in range(1,3):
    currentid = venues[i].split(',')[0].replace('\"','')
    print(currentid)
    pool.switchPort(True)
    s.cookies.clear()
    s.headers.update(headers)

    try:
        req = url+str(currentid)
        print(req)
        ip =  s.get("http://ipecho.net/plain",proxies=pool.proxies(), timeout=10)
        print(str(ip.content))
        pdata = s.get(req,proxies=pool.proxies(), timeout=10)
        #tree = html.fromstring(pdata.content)
        print(s.cookies.get_dict())
        time.sleep(0.5)
        pdata = s.get(req,proxies=pool.proxies(), timeout=10)
        print(pdata.content)
        res = open('res/res'+str(i)+'.html','w')
        res.write(str(pdata.content))
        res.close()
        #if len(tree.find_class('venueDetail'))>0:
        #    print(tree.find_class('venueName')[0].text())
    except Exception as e:
        print('exception : '+str(e))
