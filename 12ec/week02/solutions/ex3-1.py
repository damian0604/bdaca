#!/usr/bin/env python3

from collections import defaultdict

data = {'Alice': {'office': '020222', 'mobile': '0666666'},
        'Bob': {'office': '030111'},
        'Carol': {'office': '040444', 'mobile': '0644444', 'fax': "02012354"},
        "Daan": "020222222",
        "Els": ["010111", "06222"]}

myresults = defaultdict(list)

for name, entry in data.items():
    try:
        for k, v in entry.items():
            myresults[k].append(v)
    except:
        print(f"{name}'s numbers aren't stored in a dict, so I don't know what they are and will skip them")

print(myresults)
