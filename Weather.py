import json
import requests


#import os
#cwd = os.getcwd()

with open('key.json') as f:
    data = json.loads(f.read())
    key=data['key']


Web_Url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID='
#city = 'Cleveland'

Keep_Going=True
while Keep_Going:
    try:
        city=input('Please enter a city: ')   
        url = Web_Url + key + '&q=' + city   
        json_data = requests.get(url).json()
        json_data = json_data['list'][0] #need zero index, as comes as dictionary in list
        weather = json_data['weather'][0]
        Keep_Going=False
    except:
        print('NOT a real city')
        continue


#with open('data.json', 'w') as outfile:  #print json data
#    json.dump(json_data, outfile)
#
#print(json_data)
#print(json_data.keys())
#print(json_data['list'][0])


#Main = json_data['weather'][0]['main']
Description = json_data['weather'][0]['description']
print('Forcast for', city.upper())
print('-->', Description, '<--') #Not printing Main

try:
    Rain = json_data['rain']
    if len(Rain) > 0:
        for time in Rain.keys():
            print('It will rain:', Rain[time], 'mm, for:', time)
    elif len(Rain) == 0:
        print('No rain today!!!')
except:
    print('No rain today!!!')



