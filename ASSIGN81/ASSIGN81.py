#WAP to chop words from input text file, sort alphabetically
#and remove the redundant words and finally
#print the list of words.

fname = input('\n\t Enter file name: ')
finout = open(fname)
first = list()      #creates a list of lines, then into list of words
last = list()       #creates final list minus repeated words

for line in finout:
    line = line.rstrip()  #strip the whitespace from print
    words = line.split()  # chop the words
    first = first + words  #add all chopped words and make list

first.sort() #alphabetizing

for word in first:        #creates final desired final list
        if word not in last:
            last.append(word)


print(last)
