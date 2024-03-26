# Mantıksal Operatorler
"""
>
<
==
>=
<=
!=
and
or
not

"""

print(4 > 5)
print(1< 2 < 3 < 4 < 5)
print(1 >= 0)

# != eşit değil mi?
print( 1 != 0)

# 4 eşit mi? 5'e
print(4 == 5)

print(not(False)) # True
print(not(1==1)) # false

# Exercise

is_Magician = False
is_expert = True

if is_Magician and is_expert:
    print("you're a master magician")
elif is_Magician or is_expert:
    print("En azından oraya doğru gidiyorsun")
else:
    print("you're not a magician")

# is vs == logicial operator
# is, bellekteki yeri sorgular ve ona göre değer döndürür.
print(True is 1) #false
print(True is True) # True
print("1" is 1) # false
print([] is 1) # false
print(10 is 10.0) #false


