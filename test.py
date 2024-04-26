import requests
from bs4 import BeautifulSoup

# 使用requests模組，獲取網頁資訊
info = requests.get("https://practiceweb.ncue.edu.tw/p/403-1007-11-1.php?Lang=zh-tw")

# 使用BeautifulSoup模組，剖析網頁資料
soup = BeautifulSoup(info.text,"lxml")

# 獲取公告資訊標籤，並儲存成列表
all_tags = soup.find(class_="listTB table").find("tbody").find_all("tr")

Group, title, dates = [], [], []

for i in all_tags:
    Group.append(i.find('td', {'data-th': '資料群組'}).text.replace("\t","").replace("\n",""))
    title.append(i.find('td', {'data-th': '標題'}).text.replace("\t","").replace("\n",""))
    dates.append(i.find('td', {'data-th': '日期'}).text.replace("\t","").replace("\n",""))

for number in range(0,len(Group)):
    try:
        print(f"公告類別：{Group[number]}\n公告內容：{title[number]}\n公告時間：{dates[number]}")
    except:
        None