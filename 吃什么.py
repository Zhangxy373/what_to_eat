import random

with open('菜单.txt','r',encoding='utf-8') as file:
    menu_list = [line.strip() for line in file.readlines()]
menu_1=[];menu_2=[]
for i in menu_list:
    if i[0]=='1':
        menu_1.append(i)
    else:
        menu_2.append(i)

print("这是一个帮你决定下顿饭吃什么的小程序。：）")

while True:
    flag=input("要去1食堂请输入1\n要去2食堂请输入2\n随机请输入3\n退出程序输入0\n")
    if flag=='0':break
    
    input_1=input('请问我：吃什么？')
    if input_1=='吃什么？':
        if flag=='1':
            ans=random.choice(menu_1)
            print(ans)
        if flag=='2':
            ans=random.choice(menu_2)
            print(ans)
        if flag=='3':
            ans=random.choice(menu_list)
            print(ans)
    else:
        print('不问我就不告诉你！')
    input()
    
import random

with open('菜单.txt','r',encoding='utf-8') as file:
    menu_list = [line.strip() for line in file.readlines()]
menu_1=[];menu_2=[]
for i in menu_list:
    if i[0]=='1':
        menu_1.append(i)
    else:
        menu_2.append(i)

print("这是一个帮你决定下顿饭吃什么的小程序。：）")

while True:
    flag=input("要去1食堂请输入1\n要去2食堂请输入2\n随机请输入3\n退出程序输入0\n")
    if flag=='0':break
    
    input_1=input('请问我：吃什么？')
    if input_1=='吃什么？':
        if flag=='1':
            ans=random.choice(menu_1)
            print(ans)
        if flag=='2':
            ans=random.choice(menu_2)
            print(ans)
        if flag=='3':
            ans=random.choice(menu_list)
            print(ans)
    else:
        print('不问我就不告诉你！')
    input()
