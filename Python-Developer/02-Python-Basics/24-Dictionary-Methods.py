# Dictionary Methods


# .get()

user = {
    "name": "Kenan",
    "greet": "hello",
}

#  .get, dict içerisinde verinin var olup olmadığını kontrol etmek.

# "age"'den sonra eğer "age" yoksa 55'i kullan
print(user.get("age", 55))

# Dict içerisinde in ile dönüp verinin varlığını kontrol etmek
print('basket' in user)

# keys ve values değerlerini in ile kontrol etmek.
print('name' in user.keys())
print("hello" in user.values())

# dict içerisinde ki tüm verileri kontrol etmek
print(user.items())

user2 = {
    'age': [24,34,44],
    'greet': 'hello',
    'age': 20
}
# dict, clear ile temizlenir.
print(user2.clear())

# copy() ile dict kopyalamak
user2 = user.copy()
print(user2)

user3 = {
    "basket": [1,2,3],
    'greet': 'hello',
    'age': 20
}

# .pop(""), belirtilen anahtar değer çiftini siler
print(user3.pop("age"))
print(user3)

# .update("": ) ile dict içerisinde ki veriyi güncelleriz.

user4 = {
    "name": "Kenan",
    "greet": "hello",
    "age": 20
}

print(user4.update({"age": 55}))
print(user4)
