# Functions - Parameters

# Positional Parametreler bir fonksiyona değişken olarak geçilir.
def say_hello(name, emoji):
    print(f"hellooooo {name} and {emoji}")

# Positional Argümanlar, bir fonksiyona sağladığımız gerçek değerler olarak kullanılır.
say_hello("Kenan",":)")
say_hello("Cibo",":(")

# Keyword Arguments
say_hello(emoji=":)", name="Ozan")