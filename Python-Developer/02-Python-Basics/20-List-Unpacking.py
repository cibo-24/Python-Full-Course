# List Unpacking - Liste paketleme

# list verilerini index'sine göre değişkenlere aktarmak. Bunu sıralı bir şekilde değişkenin verildiği indexe göre yapar
a,b,c= [1,2,3]

print(a)
print(b)
print(c)


# Index'e göre değişkenlere atanan verilerin geri kalanını başka bir değişkende tutmak için *<variableName> yazabiliriz. Bu sayede atanmayan veriler diğer değişkende tutulacaktır.

d,e,f, *other, d = [1,2,3,4,5,6,7,8,9]

print(d)
print(e)
print(f)
print(other)
print(d)



