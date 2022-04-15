#WAP to parse and extract the float type number(ASSIGN65).
text = "X-DSPAM-Confidence:    0.8475";

pos = text.find(':')
#print(pos)
part = text[pos+5:]
#print(part)
fval = float(part)
print(part)
