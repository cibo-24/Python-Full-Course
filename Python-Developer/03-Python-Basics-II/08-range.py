# range() metodu, bu metod bir aralık metodudur.

print(range(100))

for number in range(100):
    print(number)

for numbers in range(10):
    print ("***")

# bu gibi işlemlerde for dan sonra bir değişkene bile ihtiyaç duymayabiliriz. Bunun için  "_" kullanabiliriz.
for _ in range(5):
    print("Hello Kenan")

# döngü içerisinde ki belli bir kurala göre yazmak
for _ in range(0, 10, 2): # çift sayıları verir
    print(_)

# sayıları tersten yazdırmak
for _ in range(10,0,-1):
    print(_)

# range'i for döngüsüne almak
for _ in range(10):
    print(list(range(10)))

