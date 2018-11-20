import requests
from bs4 import BeautifulSoup
import bs4
import re
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
urls = ['https://my.hupu.com/127854053218810','https://my.hupu.com/181795428473465']
with open('Personurl','r') as f:
    urls.append(f.read())
f = open("Personurl","r")
lines = f.readlines()#读取全部内容
print(type(lines))
for i in range(10):
    urls.append(lines[i])
# headers = {
#     'Host': url,
#     'User-Agent': 'Mozilla/5.0 (Linux;Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit'
#                   '/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'http://www.baidu.com',
#     'Connection': 'keep-alive',
#     'Cache-Control': 'max-age=0',
#     'cookie':'_cnzz_CV30020080=buzi_cookie%7Ceb5c236c.12c9.d534.91f9.ea6e9ab0e6af%7C-1; _dacevid3=eb5c236c.12c9.d534.91f9.ea6e9ab0e6af; _HUPUSSOID=6490ebe5-f90b-4890-836a-d53ac40d3307; UM_distinctid=1607773eb19452-0a18fe73b0a4be-16386656-13c680-1607773eb1a749; cn_2815e201bfe10o53c980_dplus=%7B%22distinct_id%22%3A%20%221607773eb19452-0a18fe73b0a4be-16386656-13c680-1607773eb1a749%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201513832575%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201513832575%2C%22%24uid%22%3A%20%22eb5c236c.12c9.d534.91f9.ea6e9ab0e6af%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D%2C%22initial_view_time%22%3A%20%221513829409%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; _fmdata=0C680138303FBBBD481F771D79EA8208BD0EA820FC1FE62E9BC5288530472516B7B160AB227A7FA460E7A15ACB21BE05AB97D517393F49D2; __dacevid3=0x76b1f4b440bc2ca7; _ga=GA1.2.253669330.1514685583; __gads=ID=af272227080a83ad:T=1515373793:S=ALNI_MaKmAy9rUASx4AS_l0RM1l04T7Olw; __closeapp=1; _CLT=b0c2a05996d8b48b354e1fa4ddfc1fef; u=29491350|6Km55aeG5pav54Ot55qE5bCP6L+35byf|8ec2|4f0c39bde7068bd8bdec0ed09adaa020|e7068bd8bdec0ed0|aHVwdV9mMDNmNTE2YmZmOGQ1N2Zk; us=1cb2d6502f73003fa3921b0d3a0a90e61b1beb4cddfaed051786d92d1b4577756e329e9492ac5d9420cdc6cc7516443a6c68dd4f88af1328cdfef77afbfe9597; PHPSESSID=gab3a63o3p0qdao1glmijh0bc4; _cnzz_CV30020080=buzi_cookie%7Ceb5c236c.12c9.d534.91f9.ea6e9ab0e6af%7C-1; ua=29736303; __dacevst=7c5a5b32.d45dc41a|1516558402935'
# }
def get():
    msg = []
    teams = {}
    sexs = {}
    locations = {}
    team = 'NBA主队：'
    sex = '性别：'
    location = '所在地：'
    msg.append(sexs)
    msg.append(teams)
    msg.append(locations)
    for url in urls:
        spanmsg = {}
        req=requests.get(url)
        req.encoding = req.apparent_encoding
        soup = BeautifulSoup(req.text, 'html.parser')
        soup=soup.find('div',{'class':'personalinfo'})
        if soup!=None:
            names = soup.find_all('span')
        # print(names)

        flag=1

        for index_each,each  in enumerate(names):
            # print((each.attrs))
            if each.attrs=={'class': ['f666']}:
                ins = ''.join(str(each.text).split())
                spanmsg[ins]=index_each
        # print(spanmsg)
        if sex in spanmsg.keys():
            ms=names[spanmsg.get(sex) + 1].text
            if msg[0].get(names[spanmsg.get(sex)+1].text)==None:
                msg[0][names[spanmsg.get(sex)+1].text]=1
            else:msg[0][names[spanmsg.get(sex)+1].text]+=1
        if team in spanmsg.keys():
            if msg[1].get(names[spanmsg.get(team)+1].text)==None:
                msg[1][names[spanmsg.get(team)+1].text]=1
            else:msg[1][names[spanmsg.get(team)+1].text]+=1
        if location in spanmsg.keys():
            if msg[2].get(names[spanmsg.get(location)+1].text) == None:
                msg[2][names[spanmsg.get(location) + 1].text] = 1
            else:
                msg[2][names[spanmsg.get(location) + 1].text] += 1
        else:continue
    print(msg)
    return msg
    # print(names)
def vis(value):
    # 传进来的是一个字典[{'男': 1}, {}, {'江苏省 南京市': 1}]
    for each in value:
        showlable=[]
        shownum = []
        for i in each:
            showlable.append(i)
            shownum.append(each.get(i))
        plt.pie(shownum, labels=showlable, autopct='%d%%')
        plt.show()
msg=get()
vis(msg)
