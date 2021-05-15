from bs4 import BeautifulSoup
import requests
from event import Event
r = requests.get('https://system32.eventsentry.com/security/event/4625')
source = BeautifulSoup(r.content,"lxml")

main=source.find("table",
            attrs={"class":"table table-sm insertion_strings"})
aTags=main.find_all("td",
                attrs={"class":"nowrap"})
fields=''
for i in range(len(aTags)):
    if i%2==1:
        fields=fields+str(aTags[i].text).replace('  ',',')

fields=fields[1:]
print('a')