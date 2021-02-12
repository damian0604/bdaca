#!/usr/bin/env python3

from collections import defaultdict

data = {'Alice': {'office': '020222', 'mobile': '0666666'},
        'Bob': {'office': '030111'},
        'Carol': {'office': '040444', 'mobile': '0644444'},
        "Daan": "020222222",
        "Els": ["010111", "06222"]}

subscriptions = defaultdict(int)

for name, entry in data.items():
    if type(entry) is str:
        subscriptions[name]+=1  # this is short for subscriptions[name] =  subscriptions[name]+1 
    else:
        subscriptions[name] += len(entry)

print(subscriptions)
