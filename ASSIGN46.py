#WAP to do Assignment 4.4.

try:
    hrs = float(input("Enter Hours:"))
    rph = float(input("Enter Rate per hour:"))

except:
    print("Please enter numeric code only.")
    quit()

def computepay(h,r):
    if (h <= 40):
        p = h * r
        #print('Pay:', Pay)
    else:
        p = ((40*r) + (h - 40)*1.5*r)
        #print('Pay:', P)
    return p

print("Pay", computepay(hrs,rph))
