score = input("Enter Score: ")
try:
    score = float(score)
except :
    print("Please enter a numeric score value")
    quit()
if score < 0 :
    print("Please enter a score value in a range of 0 through 1")
    quit()
elif score > 1 :
    print("Please enter a score value in a range of 0 through 1")
    quit()
else :
    if score < 0.6 :
        grade = "F"
    elif score < 0.7 :
        grade = "D"
    elif score < 0.8 :
        grade = "C"
    elif score < 0.9 :
        grade = "B"
    else :
        grade = "A"

print (grade)
