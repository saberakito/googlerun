import requests
import re
import json


def  getData():

    link = "https://www.boss369.com/HomeSmart.aspx?lang=EN-GB"


    f = requests.get(link)
    # print(f.text)

    result = f.text.find('__EVENTVALIDATION')

    result = re.search('__EVENTVALIDATION(.*)"', f.text)
    EVENTVALIDATION = result.group(1).split('value="')

    result = re.search('__VIEWSTATEGENERATOR(.*)"', f.text)
    VIEWSTATEGENERATOR = result.group(1).split('value="')

    result = re.search('__VIEWSTATE(.*)"', f.text)
    VIEWSTATE = result.group(1).split('value="')

    value = {
        "EVENTVALIDATION": EVENTVALIDATION[1],
        "VIEWSTATEGENERATOR": VIEWSTATEGENERATOR[1],
        "VIEWSTATE": VIEWSTATE[1]
    }
    return json.dumps(value)

print(getData());
