import json
# creating .json key file

try:
    with open('key.txt', 'r') as fhandle:
        key=fhandle.read().strip()
except:
    print('No key.txt file found')
    key=input('please enter key here: ')
    
    with open('key.txt', 'w') as outfile:  #print json data
        outfile.write(key) 
    

with open('key.json', 'w') as outfile:  #print json data
    
    dic={'key': key}    
    json.dump(dic, outfile)
    print('SUCCESS key has been dumped into json file')


#with open('key.json') as f:
#    data = json.loads(f.read())
#    print(data)