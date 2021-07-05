# Defining the function computePay
def computePay(Hours, Rate):
    h = float(Hours)
    r = float(Rate)
    if h > 40 :
        pay = 40 * r + (h - 40) * r * 1.5
    else :
        pay = h * r
    return pay

# accepting input and invoking the function computePay
hrs = input("Enter Hours:")
r = input("Enter Rate/Hour:")
print ("Pay",computePay(hrs,r))
