import os
import requests
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
for x in web:
    if x[-1:] == "\n":
        x = x[-1:]


for x, p, w in zip(name, page, web):
    print(x)
    os.mkdir(x)
    os.chdir(x)
    for s in range(1, int(p) + 1):
        url = requests.get(w + f"/{s}.jpg", stream=True)
        with open(os.getcwd() + f"/{s}.jpg", "wb") as fp:
            for chunk in url:
                fp.write(chunk)
    os.chdir("../")
