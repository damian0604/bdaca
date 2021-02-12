#!/usr/bin/env python3

names = ["Alice", "Bob", "Carol", "Damian"]
office = ["020222", "030111", "040444"]
mobile = ["0666666", "0622222", "0644444"]

if len(names) == len(office) == len(mobile):
    mydict ={}
    for n, o, m in zip(names, office, mobile):
        mydict[n] = {"office":o, "mobile":m}
    print(mydict)
else:
    print("Your data seems to be messed up - the lists do not have the same length")
