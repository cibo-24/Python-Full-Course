# Tuple - Dğeiştirilemez List

# Tuple, listeler gibidir, ancak listelerden farklı olarak onları değiştiremeyiz.

my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

# Değiştirilmesini istemediğimiz verileri "tuple" ile yazabiliriz.

# dict içerisinde ki veriler (key,value) aslında tuple içerisindedir. O yüzden dict içerisindeki verilerde değiştirilemez.

your_tuple = (24,25,26,27)
new_tuple = your_tuple[1:4]
print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(other)

# Tuple'ın sadece 2 methodu vardır. count() ve index()

there_tuple = (1,2,3,4,5,5)

# .count() ile tuple içerisinde kaç tane aynı veriden var onu sayar.
print(there_tuple.count(5))

# .index() ile seçilen index'te hangi veri var onu döndürür.
print(there_tuple.index(5))
print(len(there_tuple))