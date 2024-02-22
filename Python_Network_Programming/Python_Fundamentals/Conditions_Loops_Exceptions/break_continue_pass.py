# break
for i in range(10):
    if i == 7:
        break
    print(i)

# continue
l1 = [4, 5, 6]
l2 = [10, 20, 30]
for i in l1: # This will return a boolean value i.e. True or False
    for j in l2:
        if j == 20:
            continue
        print(i*j)  # if continue is executed, this will be skipped
    print("outside the nested loop")

# pass - just a placeholder for future changes
for i in range(10):
    pass  # this will help to avoid syntax error, you can update this for loop later as needed.
