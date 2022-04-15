# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0
c = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        pos = line.find(':')
        part = line[pos+1:]
        fval = float(part)
        s = s + fval
        c = c + 1
fvavg = s/c
print("Average spam confidence:", fvavg)
