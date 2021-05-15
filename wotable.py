from bs4 import BeautifulSoup
import requests
from event import Event
url='https://system32.eventsentry.com/security/event/563'
r = requests.get(url)
source = BeautifulSoup(r.content, "lxml")
main = source.find("div",attrs={"class": "code"})
pre = main.find("pre")
fields = pre.text
print(fields)