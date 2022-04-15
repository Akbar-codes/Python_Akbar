#WAP to check  figure out the distribution by hour of the day for each of the messages.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fin = open(name)                             #file handle

store = dict()

for line in fin:                             #searches 'From ' lines and parses
    line = line.strip()                      #removes right whitespace
    if line.startswith('From '):             #target test condition
        line = line.split()                  #words parsed out of target lines
        line = line[5]                       #gets the 6th word or the time string
        line = line[0:2]                     #gets the hour in HH:MM:SS
        store[line] = store.get(line,0) + 1  #stores the HH hour

fir = list()                                 #new list created

for value,count in store.items():            #searches 'From ' lines and parses
    fir.append((value,count))                #email sender acquired

fir.sort()                                   #sorts the newly appended list
                                             #which was in random order
for value,count in fir:                      #because dictionaries store
    print(value, count)                      #randomized tuples.
