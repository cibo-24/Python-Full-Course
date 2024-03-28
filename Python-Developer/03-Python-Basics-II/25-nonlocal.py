# Scope - nonlocal

# outer func içerisinde bulunan x değişkenini, inner func içerisinde kullanıyoruz.
# yerel olmayan değişkeni kullanmak için "nonlocal" keyword'ünü kullanırız. Yani global olmayan bir değişken.

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)

    inner()
    print("outer", x)

outer()