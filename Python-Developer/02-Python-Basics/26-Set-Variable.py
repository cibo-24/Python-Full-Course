# Set Data Type - Küme

# Set, nesnelerin sıralanmamış bir koleksiyonudur.

# set, sadece benzersiz olanları döndürür. Mükerrer(aynı) olanları döndürmez
my_Set = {1,2,3,4,5,6,6}
my_Set.add(100)
my_Set.add(200)
my_Set.add(2) # 2, olduğu için eklenmez. Mükerrer
print(my_Set)

# list içerisinde ki verileri set ile sarmalamak

my_list = [1,2,3,4,5,5]
print(set(my_list))

# set, index olarak erişmeye izin vermez.

your_set = {1,2,3,4,5,6,6}
print(2 in my_Set)
print(len(your_set))
there_set = your_set.copy()
print(there_set)
print(there_set.clear())

# Set Methods

you_set = {1,2,3,4,5}
we_set = {4,5,6,7,8,9,10}

# set içerisinde ki verilerin farklarını gösterir.
print(you_set.difference(we_set)) # 1,2,3

# set içerisinde ki veriyi atar
print(you_set.discard(5))

# 2 set arasında keşisen noktaları, ortak kümeyi bulur.
print(you_set.intersection(we_set))

# 2 setin birbiriyle kesiştiğini noktaları var mı ?
print(you_set.isdisjoint(we_set))

# 2 seti birleştir ve mükerrer olanları çıkar
print(you_set.union(we_set)) # (you_set | we_set) aynı şeyi verir.







