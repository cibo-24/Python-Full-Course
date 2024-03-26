# İterable - Yineleme
# -list, dictionary, tuple, set, string
# iterable -> one by one check each item in the collection

# dictionary
user = {
    "name": "Golem",
    "age": 5006,
    "con_swim": False,
}

# eğer user object'nin hem anahtarlarına hemde değerlerine erişmek istiyorsam .items() metodunu yazmam gerekir.
for item in user.items():
    print(item)

# sadece değerlere erişmek için values() kullanabilirim.
for item in user.values():
    print(item)

# anahtar değerlerine erişmek için ise .keys() kullanırım.
    for item in user.keys():
        print(item)