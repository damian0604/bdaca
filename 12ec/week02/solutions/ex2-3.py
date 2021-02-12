#!/usr/bin/env python3

data = {'Alice': {'office': '020222', 'mobile': '0666666'},
        'Bob': {'office': '030111'},
        'Carol': {'office': '040444', 'mobile': '0644444'},
        "Daan": "020222222",
        "Els": ["010111", "06222"]}

def get_number_of_subscriptions(x):
    if type(x) is str:
        return 1
    else:
        return len(x)

for k, v in data.items():
    print(f"{k} has {get_number_of_subscriptions(v)} phone subscriptions")
