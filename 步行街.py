#encoding=utf-8
import requests
import re as RE
from  bs4 import BeautifulSoup
import jieba
import matplotlib.pyplot as plt
class HUPU():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    rooturl='https://bbs.hupu.com/bxj'
    hupuurl='https://bbs.hupu.com'
    url=0
    Title=[]
    URL=[]
    #得到50页的帖子的url和标题
    def getContent(self):
        fp=open('bxj.txt','w+')
        for i in range(5000):
            re=requests.get(self.rooturl+'-%s'%i)
            re.encoding=re.apparent_encoding
            soup = BeautifulSoup(re.text, 'html.parser')
            lable=soup.find_all('div',attrs={"class":"titlelink box"})
            for each in lable:
                # self.url+=1;
                a=each.find('a')
                if RE.search('[0-9]',a['href']):
                     # self.URL.append(self.hupuurl + a['href'])
                     fp.write(str(a.text)+ '\n')
                     # self.Title.append(str(a.text))
        print('抓取贴子标题和url完成！')
    #将标题写入bxj.txt
    def Write(self):
        fp=open('bxj.txt','w+')
        for each in self.content:
            fp.write(each+'\n')
    #利用jieba来分词
    def SplitMessage(self):
        txt = open("bxj.txt", "r", encoding='utf-8').read()
        words = jieba.lcut(txt)  # words全部截取
        counts = {}
        for word in words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        sd=sorted(counts.items(),key=lambda asd:asd[1],reverse=True)
        num=[]
        lable=[]
        for each in sd[:20]:
            each=list(each)
            lable.append(each[0])
            num.append(each[1])
        self.Visable(num,lable)
        # with open('bxj_result.txt', 'w') as f:
        #     for i in counts:
        #         f.write(i+'\n')
    #将内容写入content中当做语料库
    def Visable(self,data, lables):
        # plt.bar(range(len(data)), data)
        plt.bar(left=range(len(lables)), height=data, align="center")
        plt.xticks(range(len(lables)), lables)
        plt.show()
    def WriteContent(self):
        s=0
        with open('content.txt', 'w', encoding='utf-8') as f:
            for each in self.URL:
                try:
                    s+=1
                    print(each)
                    re=requests.get(each)
                    re.encoding=re.apparent_encoding
                    soup=BeautifulSoup(re.text,'html.parser')
                    con = soup.find('div', {'class': 'quote-content'})
                    p = con.find_all('p')
                    for each in p:
                        f.write(each.text+'\n')
                    if s>=200:
                        break
                except:
                    print('错误出现在:'+str(each))
                    continue
        print('语料录入完成')
    def SSh(self):
        print('method begin')
        titleURL=[]
        f=open('Personurl','w')
        url='https://bbs.hupu.com/vote-'
        hur='https://bbs.hupu.com'
        print('url begin')
        for each in range(1,2):
            url= url + "{0}".format(str(each))
            re=requests.get(url)
            re.encoding=re.apparent_encoding
            soup=BeautifulSoup(re.text,"html.parser")
            content=soup.find_all('a',{'class':'truetit'})
            for each in content:
                ar=hur+each['href']
                titleURL.append(ar)
        print('personurl begin')
           # 找到个人主页的链接
        for each in titleURL:
            re=requests.get(each)
            re.encoding=re.apparent_encoding
            soup=BeautifulSoup(re.text,'html.parser')
            names=soup.find_all('a',{'class':'headpic'})
            for each in names:
                href=each['href']
                f.write(href+'\n')
        print('end')
    def getPersonalMsg(self):
        nameURL=[]
        lines=1
        for line in open("Personurl"):
            nameURL.append(line)
            lines+=1
            if lines>50:
                break
        print('get message begin')
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
        for url in nameURL:
            spanmsg = {}
            req = requests.get(url)
            req.encoding = req.apparent_encoding
            soup = BeautifulSoup(req.text, 'html.parser')
            soup = soup.find('div', {'class': 'personalinfo'})
            if soup != None:
                names = soup.find_all('span')
            # print(names)

            flag = 1

            for index_each, each in enumerate(names):
                # print((each.attrs))
                if each.attrs == {'class': ['f666']}:
                    ins = ''.join(str(each.text).split())
                    spanmsg[ins] = index_each
            # print(spanmsg)
            if sex in spanmsg.keys():
                ms = names[spanmsg.get(sex) + 1].text
                if msg[0].get(names[spanmsg.get(sex) + 1].text) == None:
                    msg[0][names[spanmsg.get(sex) + 1].text] = 1
                else:
                    msg[0][names[spanmsg.get(sex) + 1].text] += 1
            if team in spanmsg.keys():
                if msg[1].get(names[spanmsg.get(team) + 1].text) == None:
                    msg[1][names[spanmsg.get(team) + 1].text] = 1
                else:
                    msg[1][names[spanmsg.get(team) + 1].text] += 1
            if location in spanmsg.keys():
                if msg[2].get(names[spanmsg.get(location) + 1].text) == None:
                    msg[2][names[spanmsg.get(location) + 1].text] = 1
                else:
                    msg[2][names[spanmsg.get(location) + 1].text] += 1
            else:
                continue
        print(msg)
        return msg
    def vis(self,value):
        lables=['男女分布比例','主队分布比例','地域分布比例']
        # 传进来的是一个字典[{'男': 1}, {}, {'江苏省 南京市': 1}]
        #将dic 转成list 得到各个属性的值，然后画图
        for each in value:
            showlable = []
            shownum = []
            for i in each:
                showlable.append(i)
                shownum.append(each.get(i))
            plt.title(lables[value.index(each)], fontsize=20)

            plt.pie(shownum, labels=showlable, autopct='%d%%')
            plt.show()
    def cut(self):
        print()
hupu=HUPU()
# hupu.getContent()
# hupu.WriteContent()
# hupu.SplitMessage()
# msg=hupu.SSh()
msg=hupu.getPersonalMsg()
hupu.vis(msg)