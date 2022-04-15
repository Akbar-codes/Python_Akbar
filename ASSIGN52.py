max = None
min = None

while True:
    try:
        x = input("Enter a number: ")
        if x == "done":
            break

        x = int(x)
        if max is None or max < x:
            max = x
        elif min is None or min > x:
            min = x

    except ValueError:
        print("Invalid input")
        #quit()


print("Maximum is", max)
print("\nMinimum is", min)
del max
del min
del x
