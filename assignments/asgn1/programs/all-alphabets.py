import string
lower_case = [string.ascii_lowercase]
upper_case = [string.ascii_uppercase]
print(lower_case)
print(upper_case)
str = input('input a string ')
print(str)
trigger = 0
l1 = len(lower_case)
l2 = len(str)
for i in range(l1):
    for j in range(l2):
        if lower_case[i] == str[j]:
            trigger = 1
            print(trigger)
        else:
            trigger = 0
    if trigger == 1:
        found = [lower_case[i]]
        print(found)
    else:
        not_found = [lower_case[i]]
        print(not_found)
"""print('elements found in string are: ',found)
print('elements found in string are: ',not_found)"""