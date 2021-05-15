from bs4 import BeautifulSoup
import requests
from event import Event,totalEvent
import csv

r = requests.get('https://system32.eventsentry.com/security/events')
source = BeautifulSoup(r.content,"lxml")

main=source.find("table",
            attrs={"class":"table table-sm"})
aTags=main.find_all("a")

events=[]
totalevents=[]
for i in range(len(aTags)):
    splitted=str(aTags[i].text).split('-')
    event=Event(splitted[0],splitted[1])
    events.append(event)

for i in range(len(events)):
#for i in range(5):
    url='https://system32.eventsentry.com/security/event/'+str(events[i].name).replace(' ','')
    r = requests.get(url)
    source = BeautifulSoup(r.content, "lxml")
    try:
        main = source.find("table",
                           attrs={"class": "table table-sm insertion_strings"})
        aTags = main.find_all("td",
                              attrs={"class": "nowrap"})
        fields = ''
        for j in range(len(aTags)):
            if j % 2 == 1:
                fields = fields + str(aTags[j].text).replace('  ', ',')

        fields = fields[1:]
        event=totalEvent(events[i].name.strip(),events[i].exp[1:],fields)
        totalevents.append(event)
        print(str(events[i].name)+' tablosu var')
        continue
    except:
        try:
            main = source.find("div",attrs={"class": "code"})
            pre = main.find("pre")
            fields = '-'+pre.text
            event=totalEvent(events[i].name.strip(),events[i].exp[1:],fields)
            totalevents.append(event)
            print(str(events[i].name) + ' tablosu yok')
        except Exception as e:
            print('sorun var'+str(events[i].name).replace(' ','') +'da-'+str(e))


filename = 'WEDesc.csv'
try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for item in totalevents:
            writer.writerow([item.name, item.exp, item.fields])
except BaseException as e:
    print('BaseException:', filename)
else:
    print('Data has been loaded successfully !')
print('a')