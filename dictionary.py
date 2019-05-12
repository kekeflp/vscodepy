# __*__ coding = uft-8 __*__
'''
number = {"name": "xiaoming", "max": 5, "mix": 1, "age": 18, "gender": "男"}
print(number)
for k, v in number.items():
    print("key：" + k)
    print("value：" + str(v))
'''

aliens = []
# 生成列表中30个元素
for alien_number in range(0, 30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# print(aliens)
# 显示前5个
for number in aliens[:5]:
    print(number)

print("...")

print("Total number of aliens: " + str(len(aliens)))

# 把列表aliens中的30个字典，变成不一样的类型
for i in aliens[0:3]:
    if i["color"] == "green":
        i["color"] = "red"
        i["points"] = 15
        i["speed"] = "fast"


for number in aliens[:10]:
    print(number)

# 将列表插入词典
# pizza = {"crust": "thick", "toppings": ["nushrooms", "extra cheese"]}
