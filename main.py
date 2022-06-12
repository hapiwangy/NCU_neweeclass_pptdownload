import os
import requests
import copy
basic = "https://ncueeclass.ncu.edu.tw"
name = []
page = []
web = []
with open("name.txt", "r") as fp:
    for x in fp.readline().split():
        name.append(x)
with open("page.txt", "r") as fp:
    for y in fp.readline().split():
        page.append(y)
with open("web.txt", "r") as fp:
    for x in fp.readlines():
        web.append(basic + x)
for x, p, w in zip(name, page, web):
    print(x)
    os.mkdir(x)
    os.chdir(x)
    if w[-1] != 's':
        we = w[:-1]
    else:
        we = w 
    for s in range(1, int(p) + 1):
        print(we + f"/{s}.jpg")
        url = requests.get(we + f"/{s}.jpg", stream=True)
        with open(os.getcwd() + f"/{s}.jpg", "wb") as fp:
            for chunk in url:
                fp.write(chunk)
    os.chdir("../")
