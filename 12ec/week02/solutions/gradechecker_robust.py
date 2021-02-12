#!/usr/bin/env python3

grades = [4, 7.8, -3, 3.6, 12, 9.1, "4.4", "KEGJKEG", 4.2, 7, 5.5]

for grade in grades:
    try:
        grade_float = float(grade)
        if grade_float >10:
            print(grade_float,'is an invalid grade')
        elif grade_float <1:
            print(grade_float,'is an invalid grade')
        elif grade_float >= 5.5:
            print(grade,'is a PASS')
        else:
            print(grade,'is a FAIL')

    except:
        print('I do not understand what',grade,'means')

