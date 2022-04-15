#WAP to check which user has been the most prolific committer 
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fin = open(name)                             #file handle

fir = list()

for line in fin:                             #searches 'From ' lines and parses
    line = line.strip()                      #removes right whitespace
    if line.startswith('From '):             #target test condition
        line = line.split()                  #words parsed out of target lines
        fir.append(line[1])                  #email sender acquired

counts = dict()                              #dictionary defined

for word in fir:                             #adds or creates new items
    counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None

for word, count in counts.items():             #checks which sender has sent most
    if bigcount is None or count > bigcount:   #emails
        bigword = word
        bigcount = count

print(bigword, bigcount)
