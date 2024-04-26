from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__, template_folder='D:/Python_Project/網路爬蟲/師培中心資訊/', static_folder='D:/Python_Project/網路爬蟲/師培中心資訊')
CORS(app)

@app.route('/')
def index():
    # 使用 requests 模組，獲取網頁資訊
    info = requests.get("https://practiceweb.ncue.edu.tw/p/403-1007-11-1.php?Lang=zh-tw")

    # 使用 BeautifulSoup 模組，剖析網頁資料
    soup = BeautifulSoup(info.text,"lxml")

    # 獲取公告資訊標籤，並儲存成列表
    all_tags = soup.find(class_="listTB table").find("tbody").find_all("tr")

    Group, title, dates, hrefs = [], [], [], []

    for i in all_tags:
        Group.append(i.find('td', {'data-th': '資料群組'}).text.replace("\t","").replace("\n",""))
        title.append(i.find('td', {'data-th': '標題'}).text.replace("\t","").replace("\n",""))
        dates.append(i.find('td', {'data-th': '日期'}).text.replace("\t","").replace("\n",""))
        hrefs.append(i.find('a')['href'])

    return render_template('index.html', data=zip(Group, title, dates, hrefs))

if __name__ == '__main__':
    app.run(debug=True)
