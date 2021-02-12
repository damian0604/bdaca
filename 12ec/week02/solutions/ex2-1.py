#!/usr/bin/env python3

names = ["Alice", "Bob", "Carol"]
office = ["020222", "030111", "040444"]
mobile = ["0666666", "0622222", "0644444"]

mydict ={}
for n, o, m in zip(names, office, mobile):
    mydict[n] = {"office":o, "mobile":m}

print(mydict)
