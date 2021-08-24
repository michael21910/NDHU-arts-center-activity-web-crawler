import requests
from bs4 import BeautifulSoup
from selenium import webdriver

name = []; out = []; urls = []; event_time = []; event_place = []
url = "https://artscenter.ndhu.edu.tw/p/403-1123-5125-1.php?Lang=zh-tw"
html = requests.get(url)
html.encoding = "utf-8"
sp = BeautifulSoup(html.text, 'lxml')
for datas in sp.select('div > div > div > div > div > div > div > div > div > div > section > div > div > div > div > div > div > a'):
    urls.append(datas.get('href'))
    name.append(datas.text.strip('\n\t'))
for datas in sp.select('div > div > div > div > div > div > div > div > div > div > section > div > div > div > div > div > div > i'):
    out.append(datas.text.strip(' '))
    
for links in urls:
    html = requests.get(links)
    html.encoding = "utf-8"
    sp = BeautifulSoup(html.text, 'lxml')
    temp = sp.find('div', 'mcont').text.strip('\n').strip('\t').strip('\r')    
    for i in range(len(temp)):
        time_temp = ""; time_count = 0
        if(temp[i] == "時" and temp[i + 1] == "間" and temp[i + 3] == "2"):
            time_count = i + 3
            while(temp[time_count] != '\n'):
                time_temp = time_temp + temp[time_count]
                time_count = time_count + 1
            event_time.append(time_temp)
            break
        if(i == len(temp) - 1 and time_count == 0):
            event_time.append('無')
            break
for links in urls:
    html = requests.get(links)
    html.encoding = "utf-8"
    sp = BeautifulSoup(html.text, 'lxml')
    temp = sp.find('div', 'mcont').text.strip('\n').strip('\t').strip('\r')    
    for i in range(len(temp)):
        place_temp = ""; place_count = 0
        if(temp[i] == "地" and temp[i + 1] == "點"):
            place_count = i + 3
            while(temp[place_count] != '\n'):
                place_temp = place_temp + temp[place_count]
                place_count = place_count + 1
            event_place.append(place_temp)
            break
        if(i == len(temp) - 1 and place_count == 0):
            event_place.append('無')
            break
            
urls = urls[0:5]
name = name[0:5]
out = out[0:5]
event_time = event_time[0:5]
event_place = event_place[0:5]
count = 1
for i in range(0, 5):
    print(str(count) + '.' + str(name[i]))
    print("發布時間：" + str(out[i]))
    print("公告連結：" + str(urls[i]))
    print("活動時間：" + str(event_time[i]))
    print("活動地點：" + str(event_place[i]))
    count = count + 1
    print()