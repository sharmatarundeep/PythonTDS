1. import random vs from random import * 
    * In case of import random - you will have to use random. to call any function of random modules Example - say random.randomint()
    * In case of from random import * - you don't need to use random. to call any function of random modules. Example - directly say randomint()

2. Every function has a return value. If you don't have a return statement in the function, by default function will return None. Also print function always return None.

3. Deep copy vs regular copy..
    * In case of regular copy both variables will point to same reference and if you change 1 other will change too
    list1 = [1,2,3,4]
    list2 = list1 # copy list 1 to list 2
    list2[1] = 5 # Both list1 and list2 will change now
    * In case of deep copy both variables will point to different reference and if you change 1 other will not change
    import copy
    list1 = [1,2,3,4]
    list2 = copy.deepcopy(list1) # deep copy list 1 to list 2
    list2[1] = 5 # only list 2 will change

4. Pyperclip - Can be used to copy something to clipboard and paste it later as needed. Example below
    import pyperclip
    pyperclip.copy("Hello")
    you can do command + v now or 
    pyperclip.paste()