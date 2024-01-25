while (True):
    try:
        num=int(input("Enter a number"))
        result=1/num
        print (result)
    except ValueError as e:
        print ("Please enter a valid number")
        print (e)
    except ZeroDivisionError:
        print ("Please dont divide by ZERO")
    else:
        break

