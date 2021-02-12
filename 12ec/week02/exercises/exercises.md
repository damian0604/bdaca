# Exercise 1: Working with lists


## 1. Warming up

- Create a list, loop over the list, and do something with each value (you're free to choose). 

## 2. Did you pass?

- Think of a way to determine for a list of  grades whether they are a pass (>5.5) or fail.
- Can you make that program robust enough to handle invalid input (e.g., a grade as 'ewghjieh')?
- How does your program deal with impossible grades (e.g., 12 or -3)?
- Any other improvements?




# Exercise 2: Working with dictionaries


- Create a program that takes lists of corresponding data (a list of first names, a list of last names, a list of phone numbers) and converts them into a dictionary. You may assume that the lists are ordered correspondingly. To loop over two lists at the same time, you can do sth like this: (of course, you later on do not want to print put to put in a dictionary):
```
for i, j in zip(list1, list):
   print(i,j)
```
- Improve the program to control what should happen if the lists are (unexpectedly) of unequal length.
- Create another program to handle a phone dictionary. The keys are names, and the value can either be a single phone number, a list of phone numbers, or another dict of the form {"office": "020123456", "mobile": "0699999999", ... ... ... }. Write a function that shows how many different phone numbers a given person has.
- Write another function that prints only mobile numbers (and their owners) and omits the rest (If you want to take it easy, you may assume that they are stored in a dict and use the key "mobile". If you like challenges, you can also support strings and lists of strings by parsing the numbers themselves and check whether they start with 06. You can check whether a string starts with 06 by checking mystring[:2]=="06" (the double equal sign indicates a comparison that will return True or False). If you like even more challenges, you could support country codes).



# Exercise 3: Working with defaultdicts

- Take the data from Excercise 2. Write a program that collects all office numbers, all mobile numers, etc. Assume that there are potentially also other categories like "home", "second", maybe even "fax", and that they are unknown byforehand.
- To do so, you can use the following approach:
```python
from collections import defaultdict
myresults = defaultdict(list)
```
Loop over the appropriate data. For all the key-value pairs (like "office": "020111111"), do ` myresults[key].append(value)`: This will append the current phone numner (02011111) to the list of "office" numbers. 
- Do you see why this works only with a defaultdict but not with a "normal" dict? What would happen with a normal dict?
- Take the function from Exercise 2 that prints how many phone numbers a given person has. Use a defaultdict instead to achieve the same result. What are the pros and cons?
