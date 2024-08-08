# Python solution file
k = input()
lowercase = [char for char in k if char.islower()]
lowercase.sort()
uppercase = [char for char in k if char.isupper()]
uppercase.sort()
digits = [char for char in k if char.isdigit()]
digits.sort()
edig = [digit for digit in digits if int(digit) % 2 == 0]
odig = [digit for digit in digits if int(digit) % 2 != 0]
ltotal = "".join(lowercase)
utotal = "".join(uppercase)
dtotal = "".join(digits)
dto = "".join(odig)
dte = "".join(edig)
kio=ltotal+utotal+dto+dte
print(kio)
