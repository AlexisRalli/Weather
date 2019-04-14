import json
import requests


key = '623bafaf516827fba2b5a2e1c329b274'
city = 'Tokyo'

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

Main = json_data['weather'][0]['main']
Description = json_data['weather'][0]['description']
Rain = json_data['rain']
print('Forcast for ', city)
print(Main, Description)

if len(Rain) > 0:
    print('It will rain: ', Rain)
elif len(Rain) == 0:
    print('No rain today!!!')