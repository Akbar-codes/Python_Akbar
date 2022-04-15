#WAP to make grade-checker based on 0.0 to 1.0 and display an error otherwise.
inp = input(" Enter Result here: ")
Res = float(inp)

if Res >= 0.0 and Res <= 1.0:
    if Res >= 0.9 and Res <= 1.0:
        print("A")
    elif Res >= 0.8 and Res < 0.9:
        print("B")
    elif Res >= 0.7 and Res < 0.8:
        print("C")
    elif Res >= 0.6 and Res < 0.7:
        print("D")
    else:
        print("F")

else:
    print("\n\n\t\tERROR 505: Just enter a no. from 0.0 to 1.0!!")
