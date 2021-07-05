largest = None
smallest = None
while True:
    num = input("Enter a number: ")
# Break if user type in "done"
    if num == "done" : break

#Check for valid integer values
    try :
        n = int(num)
    except :
        print("Invalid input")
        continue

# find Maximum
    if largest is None :
        largest = n
    else :
        if n > largest :
            largest = n

# find Minimum
    if smallest is None :
      smallest = n
    else :
        if n < smallest :
            smallest = n
if largest != None :
    print("Maximum is", largest)
if smallest != None :
    print("Minimum is", smallest)
