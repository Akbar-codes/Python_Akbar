#WAP to find line that start specifically with "From " string, then chop all those lines
#and print 2nd word. Also count how many such words are there and print it.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

words = list()
fin = open(fname)
count = 0

for line in fin:                #loop to read through each lines
    line = line.rstrip()        # strip right whitespace
    if line.startswith('From '):#Test expression
        words = line.split()    #parse the line into words
        print(words[1])
        count = count + 1       #counter var

print("There were", count, "lines in the file with From as the first word")
