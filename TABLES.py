#WAP to print table of any number the user asks.
#Users may forget their tables so this helps.
print('\n\n\n\t\t\t TABLES! ')
print('\n\n\n\n\t\t You can enter any number to see its tables. ')
print('\n\t\t Just enter the number ')
a = float(input('\t\t'))
print('\n')
i = 1
while i<=10:#Loop to print the table.
    b=(a*i)
    print('\t\t',a,'x',i,'=',b)
    i=i+1

print('\n\t\t There you go. Although try to')
print('\n\t\t memorize them for your own benefit')
