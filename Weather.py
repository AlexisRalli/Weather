import json
import requests


key = '623bafaf516827fba2b5a2e1c329b274'
city = 'Cleveland'

url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID='
url = url + key + '&q=' + city

json_data = requests.get(url).json()
with open('data.json', 'w') as outfile:
    json.dump(json_data, outfile)
    
#print(json_data)
#print(json_data.keys())
#print(json_data['list'][0])

json_data = json_data['list'][0] #need zero index, as comes as dictionary in list
weather = json_data['weather'][0]

#Main = json_data['weather'][0]['main']
Description = json_data['weather'][0]['description']
print('Forcast for', city.upper())
print('-->', Description, '<--') #Not printing Main

try:
    Rain = json_data['rain']
    if len(Rain) > 0:
        for key, value in Rain:
            print('It will rain:', key, value, 'mm')
    elif len(Rain) == 0:
        print('No rain today!!!')
except:
    print('No rain today!!!')



