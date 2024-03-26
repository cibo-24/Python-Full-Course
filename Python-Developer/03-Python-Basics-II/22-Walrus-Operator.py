# walrus Operator

a = "hellooooooooooo"

if (len(a) > 10):
    print(f"too long {len(a)} elements")

# Yukarıda ki ifadeyi walrus sayesinde bir değişkene atayabiliriz.
    
if ((n := len(a)) > 10):
    print(f"too long {n} elements")

# a'nın uzunluğu 1'den büyük ise, uzunluğunu kısaltarak yazdır.
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]