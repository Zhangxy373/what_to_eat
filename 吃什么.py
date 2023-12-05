import random

with open('菜单.txt','r',encoding='utf-8') as file:
    menu_list = [line.strip() for line in file.readlines()]

print("这是一个帮你决定下顿饭吃什么的小程序。：）")
print("按回车生成目的地，输入0退出程序。")

while True:
    flag=input("吃什么？")
    if flag=='0':break
    ans=random.choice(menu_list)
    print(ans)

