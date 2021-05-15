from bs4 import BeautifulSoup
import requests
url='https://system32.eventsentry.com/security/event/563'
r = requests.get(url)
source = BeautifulSoup(r.content, "lxml")
try:
    main = source.find("table",
                       attrs={"class": "table table-sm insertion_strings"})
    aTags = main.find_all("td",
                          attrs={"class": "nowrap"})
    fields = ''
    for i in range(len(aTags)):
        if i % 2 == 1:
            fields = fields + str(aTags[i].text).replace('  ', ',')

    fields = fields[1:]
except:
    try:
        main = source.find("div", attrs={"class": "code"})
        pre = main.find("pre")
        fields = pre.text
    except Exception as e:
        print('sorun var' + 'da-' + str(e))