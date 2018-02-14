#!/usr/bin/env python3

grades = [4, 7.8, -3, 3.6, 12, 9.1, "4.4", "KEGJKEG", 4.2, 7, 5.5]



def check_grade(grade):
    try:
        grade_float = float(grade)
    except:
        return('INVALID')
    if grade_float >10 or grade_float <1:
        return('INVALID')
    elif grade_float >= 5.5:
        return('PASS')
    else:
        return('FAIL')


for grade in grades:
    print(grade,'is',check_grade(grade))
