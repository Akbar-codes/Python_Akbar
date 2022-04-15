fname = input("Enter file name.txt: ")
fin = open(fname)
#print(fin)

for line in fin:
    line1 = line.rstrip()
    print(line1.upper())
