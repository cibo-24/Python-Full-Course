is_old = True
is_licenced = True

# if koşulunu <DataName>: ve else if'i ise elif <DataName>: olarak giriyoruz.
# ve (&&) yerine and operatörü gelir.
# veya (||) yerine ise or operatörü gelir.

if is_old and is_licenced:
    print('you are old enough to drive!')
elif is_licenced or is_old:
    print('we are old enough to drive now!')
else:
    print("Why bro! Do you something!") 




