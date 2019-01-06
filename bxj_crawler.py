import requests
from bs4 import BeautifulSoup
import jieba
import matplotlib.pyplot as plt


class HoopCrawler:
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    url = 0
    title = []
    urls = []


    def cache(self):
        pass
    def get_content(self):
        fp = open("bxj.txt", "w+")
        for i in range(5000):
            re = requests.get(+"-%s" % i)
            re.encoding = re.apparent_encoding
            soup = BeautifulSoup(re.text, "html.parser")
            label = soup.find_all("div", attrs={"class": "titlelink box"})
            for each in label:
                # self.url+=1;
                a = each.find("a")
                if re.search("[0-9]", a["href"]):
                    # self.urls.append(self.hupuurl + a['href'])
                    fp.write(str(a.text) + "\n")
                    # self.title.append(str(a.text))
        print("抓取贴子标题和url完成！")

    # 将标题写入bxj.txt
    def Write(self):
        fp = open("bxj.txt", "w+")
        for each in self.content:
            fp.write(each + "\n")

    def split_message(self):
        txt = open("bxj.txt", "r", encoding="utf-8").read()
        words = jieba.lcut(txt)  # words全部截取
        counts = {}
        for word in words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        sd = sorted(counts.items(), key=lambda asd: asd[1], reverse=True)
        num = []
        lable = []
        for each in sd[:20]:
            each = list(each)
            lable.append(each[0])
            num.append(each[1])
        self.visable(num, lable)
        # with open('bxj_result.txt', 'w') as f:
        #     for i in counts:
        #         f.write(i+'\n')

    # 将内容写入content中当做语料库
    def visable(self, data, lables):
        # plt.bar(range(len(data)), data)
        plt.bar(left=range(len(lables)), height=data, align="center")
        plt.xticks(range(len(lables)), lables)
        plt.show()

    def WriteContent(self):
        s = 0
        with open("content.txt", "w", encoding="utf-8") as f:
            for each in self.urls:
                try:
                    s += 1
                    print(each)
                    re = requests.get(each)
                    re.encoding = re.apparent_encoding
                    soup = BeautifulSoup(re.text, "html.parser")
                    con = soup.find("div", {"class": "quote-content"})
                    p = con.find_all("p")
                    for each in p:
                        f.write(each.text + "\n")
                    if s >= 200:
                        break
                except:
                    print("错误出现在:" + str(each))
                    continue
        print("语料录入完成")

    def SSh(self):
        print("method begin")
        titleURL = []
        for each in range(1, 2):
            url = url + "{0}".format(str(each))
            res = requests.get(url)
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, "html.parser")
            content = soup.find_all("a", {"class": "truetit"})
            for each in content:
                ar = hur + each["href"]
                titleURL.append(ar)
        print("personurl begin")
        # 找到个人主页的链接
        for each in titleURL:
            res = requests.get(each)
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, "html.parser")
            names = soup.find_all("a", {"class": "headpic"})
            for each in names:
                href = each["href"]
                f.write(href + "\n")
        print("end")

    def get_person_msg(self):
        nameURL = []
        lines = 1
        for line in open("Personurl"):
            nameURL.append(line)
            lines += 1
            if lines > 50:
                break
        print("get message begin")
        msg = []
        teams = {}
        sexs = {}
        locations = {}
        team = "NBA主队："
        sex = "性别："
        location = "所在地："
        msg.append(sexs)
        msg.append(teams)
        msg.append(locations)
        for url in nameURL:
            spanmsg = {}
            req = requests.get(url)
            req.encoding = req.apparent_encoding
            soup = BeautifulSoup(req.text, "html.parser")
            soup = soup.find("div", {"class": "personalinfo"})
            if soup != None:
                names = soup.find_all("span")
            # print(names)

            flag = 1

            for index_each, each in enumerate(names):
                # print((each.attrs))
                if each.attrs == {"class": ["f666"]}:
                    ins = "".join(str(each.text).split())
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

    def vis(self, value):
        lables = ["男女分布比例", "主队分布比例", "地域分布比例"]
        # 传进来的是一个字典[{'男': 1}, {}, {'江苏省 南京市': 1}]
        # 将dic 转成list 得到各个属性的值，然后画图
        for each in value:
            showlable = []
            shownum = []
            for i in each:
                showlable.append(i)
                shownum.append(each.get(i))
            plt.title(lables[value.index(each)], fontsize=20)

            plt.pie(shownum, labels=showlable, autopct="%d%%")
            plt.show()

    def cut(self):
        print()


hupu = HoopCrawler()
hupu.get_content()
# hupu_crawler.WriteContent()
# hupu_crawler.split_message()
# msg=hupu_crawler.SSh()
msg = hupu.get_person_msg()
hupu.vis(msg)
