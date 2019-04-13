import json
import urllib

key='623bafaf516827fba2b5a2e1c329b274'

url='http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={'+ key +'}'
responce= urllib.urlopen(url)