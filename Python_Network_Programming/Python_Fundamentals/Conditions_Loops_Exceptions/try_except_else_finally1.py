# try except and else
"""
try:
    print (10/1)
except:
    print("Error")
else:
    print("Done, no exception raised")"""

# try except and finally
try:
    print (10/1)
except:
    print("Error")
finally:
    print("I dont care, I will get executed either way")

# error case
try:
    print (10/0)
except:
    print("Error")
finally:
    print("I dont care, I will get executed either way")