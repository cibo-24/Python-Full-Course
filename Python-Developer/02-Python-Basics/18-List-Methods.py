# List Methods

basket = [1,2,3]
len(basket) # dizinin boyutunu hesaplar.

# adding - ekleme

# append()
football = [1,2,3,4,5]
football.append(600)
print(football)

# insert() -> seçilen veriden sonra yeni veri ekler.
football.insert(600, 100)
print(football)

# extend() -> diziyi genişleterek yazılan veriyi dizinin üzerine ekler.
football.extend([101,102])
print(football)

# Removing Methods

# pop(), dizinin sonunda ki veriyi kaldırır. Veya index'e göre veri kaldırır.
football.pop()
football.pop(1)
print(football) 

# remove(), girilen veriyi kaldırır.
football.remove(600)
print(football)

# clear(), arrays içerisinde ki her şeyi kaldırır.
football.clear()
print(football)


# LIST METHODS - 2

# index(), girilen verinin hangi indexte olduğunu bulur.
tennis = ["a","b","c","d","e"]
print(tennis.index("d"))

# in, dizi içerisinde veri kontrolü yapar
print ("b" in tennis) # true
print("x" in tennis) # false
print("n" in "hi my name is Kenan") # true

# count(), arrays içerisinde ki verinin kaç kere var olduğunu döner

print(tennis.count("e")) # 1


# LIST METHODS - 3

ruby = ["a", "b", "c", "d", "e","c","x","a"]

# sort(), array'i yeniden sıralamaya yarar
ruby.sort()
print(ruby)

number = [1,11,2,34,23,12,56,90,3,4,5,13]
number.sort()
print(number)

# copy(), listenin kopyasını alıp başka bir değişkene atar.
new_number = number.copy()
print(new_number)

# reverse(), arrays'teki verilerin index numarasını değiştirerek tersten yazar.
number.reverse()
print(number)
