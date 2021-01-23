'''https://inputtools.google.com/request?text=a&itc=hi-t-i0-und&num=13&cp=0&cs=1&ie=utf-8&oe=utf-8&app=demopage'''

import os
import sys
import csv
import http.client
import json
import requests
from fake_useragent import UserAgent

def request(ch):
    #conn  =  http.client.HTTPSConnection('inputtools.google.com')
    #conn.request('POST' , '/request?text=' + ch + '&itc=hi-t-i0-und&num=13&cp=0&cs=1&ie=utf-8&oe=utf-8&app=demopage')
    ua = UserAgent()
    user_agent = ua.random
    headers = {'user-agent': user_agent,}
    r = requests.get('https://inputtools.google.com/request?text=' + ch + '&itc='+sys.argv[-1]+'-t-i0-und&num=13&cp=0&cs=1&ie=utf-8&oe=utf-8&app=demopage', headers=headers)
    res = r.json()
    #out = json.loads(res.read().decode('utf-8'))
    dict = {}
    dict[res[1][0][0]] = res[1][0][1]
    return dict

def test(new_dict,i,d, count, c):
    time.sleep(5)
    g_data = request(i)
    print(d[i])
    print(g_data)
    new_dict[i] = []
    if(d[i] in g_data[i]):
        if(d[i]==g_data[i][0] or d[i]==g_data[i][1]):
            new_dict[i].append(d[i])
        else:
            new_dict[i].append(g_data[i][0])
            new_dict[i].append(g_data[i][1])
            new_dict[i].append(d[i])
            count = count +1
    else:
        new_dict[i].append(g_data[i][0])
        new_dict[i].append(g_data[i][1])
        new_dict[i].append(d[i])
        c = c +1
    return new_dict, count, c


with open(sys.argv[-2], 'r') as f:
    data = f.readlines()
    d = {}
    count = 0
    for i in data:
            a = i.split(',')
            d[a[0].strip()] = ''
            count = count+1


print(len(d))

count = 0
c =0
new_dict={}
for i in d: 
    try:
        g_data = request(i)
        #print(d[i])
        print(g_data)
        new_dict[i] = []
        if(d[i] in g_data[i]):
            if(d[i]==g_data[i][0] or d[i]==g_data[i][1]):
                new_dict[i].append(d[i])
            else:
                new_dict[i].append(g_data[i][0])
                new_dict[i].append(g_data[i][1])
                new_dict[i].append(d[i])
                count = count +1
        else:
            new_dict[i].append(g_data[i][0])
            new_dict[i].append(g_data[i][1])
            new_dict[i].append(d[i])
            c = c +1
    except:
        new_dict, count, c = test(new_dict,i,d, count, c)
        

print("Number of Lines in the text File. ", len(new_dict))
    



