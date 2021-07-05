fname = input("Enter file name: ")
fhandle = open(fname,"r")
#content = fhandle.read()
for line in fhandle:
    uppercontent = line.upper()
    print(uppercontent.rstrip())
