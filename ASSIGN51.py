s = 0
c = 0

while True:
    x = float(input("\n\n\t\t Enter a number: "))
    y =  input("Would you like to continue?(Yes/Done): ")
    c += 1
    s += x
    if y == "Done":
        break
    print(x)
print("All done there.")
print("The count of numbers entered", c, "and sum", s, "finally average", s/c)
del s
del c
del x
del y
