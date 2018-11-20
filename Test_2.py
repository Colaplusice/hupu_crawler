msg=[['男', '浙江省杭州市', '火箭', '小黑屋住户'], ['男', '上海市闵行区']]
'NBA主队'
'性别'
'所在地'
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
sex={}
city={}
team={}
value=[]
value.append(sex)
value.append(city)
value.append(team)
for each in msg:
    if len(each)==0:
        continue
    elif len(each)==1:
        each.append('null')
        each.append('null')
    elif len(each)==2:
        each.append('null')
    for i in range(0,3):
            if value[i].get(each[i])=='null':
                print('null')
                continue
            elif value[i].get(each[i])==None:
                value[i][each[i]]=1

            else:
                value[i][each[i]]+=1
print(value)
for each in value:
    showlable=[]
    shownum=[]
    for i in each:
        showlable.append(i)
        shownum.append(each.get(i))
    plt.pie(shownum,labels=showlable, autopct='%d%%')
    plt.show()

# labels=['男','女']
# plt.pie([sex['男'],sex['女']],labels=labels,autopct='%d%%')
# plt.show()
# print(sex)
# rate = [1, 7, 3, 9]
# explode = [0, 0, 0.1, 0]
# colors = ['c', 'm', 'y', 'g']
# labels = ['Apple', 'Pear', 'Peach', 'Orange']
#
# plt.pie(rate, explode=explode, colors=colors, labels=labels, autopct='%d%%')
#
# plt.show()