# __*__ coding=utf-8 __*__

# 邀请嘉宾
personlist = ["小赵", "小钱", "小孙"]
print("本次会议邀请的嘉宾有： %s、 %s、 %s。" % (personlist[0],
                                   personlist[1], personlist[2]))
print("但是[%s]可能因为有事而无法到达！" % personlist[1])
print("===="*10)
# list.pop(下标)删除指定下标的值，后面的值自动往前补位，且删除的值还能被捕获而使用
notaccept = personlist.pop(1)
# list.insert(下标，值)，在指定的下标处插入一个新值，原下标处的值往后挪一位
personlist.insert(1, "小李")
print("现在将[%s]替换为[%s]，以下是重新刷新邀请人员名单： %s、 %s、 %s。" % (notaccept, personlist[1], personlist[0],
                                                     personlist[1], personlist[2]))
for item in personlist:
    print("="*30)
    print("诚意的邀请[%s]，您来出席本次会议!\r" % item)

print("+"*30)
print("临时决定还要添加一位人员：小周")
# 在列表尾部追加
personlist.append("小周")
print(personlist)
print("+"*30)

print("会议开始！")
print("45分钟后。。。。")
print("[%s] 临时有事，已离场！" % personlist.pop())
print("60分钟后。。。。")
print("[%s] 临时有事，已离场！" % personlist.pop())
print("目前现场还剩2位人员，分别是：[%s]、[%s]" % (personlist[0], personlist[1]))
print("120分钟后。。。。")
print("会议结束！")
del personlist[1]
del personlist[0]
print("+"*30)
# 在Python中，False,0,'',[],{},()都可以视为假
if personlist:
    print("还有人未离场！")
else:
    print("所有人已经全部离场！")
print("+"*30)