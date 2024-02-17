# Dictionary - Sözlük, diğer dillerde hash tablosu, harita ya da nesneler(object) olarak adlandırlabilir.

# Python Diliyle, dict, bu bizim anahtar ve değer çiftleri yaratmamızı sağlar.

dictionary = {
    "a":1,
    "b":2,
    "c":3,
}

# dict verisine ulaşmak
# dictionary, index olarak sıralanmamış bir anahtar-değer çiftidir.
print(dictionary)
print(dictionary["b"])
print(dictionary["c"])


# dict, içerisinde her veri türünü tutabilir.

new_dictionary = {
    "a": [1,2,3],
    "b": "hello",
    "x": True
}

# dict'in a keywordünün 1.indexine ulaşır.
print(new_dictionary["a"][1])

my_list = [
    {
    "a": [1,2,3],
    "b": "hello",
    "x": True
    },
    {
    "a": [4,5,6],
    "b": "hello",
    "x": True
    }
]
# my_list, 0.indexinde bulunan verinin "a"'nın 2.indexi
print(my_list[0]["a"][2])