#WAP to do Assignment 3.1.

try:
    hrs = float(input("Enter Hours:"))
    rph = float(input("Enter Rate per hour:"))

except:
    print("Please enter numeric code only.")
    quit()

if (hrs <= 40):
    Pay = hrs * rph
    print('Pay:', Pay)
else:
    Pay = ((40*rph) + (hrs - 40)*1.5*rph)
    print('Pay:', Pay)
