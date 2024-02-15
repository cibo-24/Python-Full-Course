# List, herhangi bir türde olabilen nesnelerin sıralı bir dizisidir.
# Array ile aynı şeydir. Python'da List denir.

li = [1,2,3,4,5]
li2 = ["a", "b", "c"]
li3 = [1,2,"a", True] 

# Data Structure - Veri Yapıları
# Verileri bir klasör veya kutu içerisinde :) organize etmemizin bir yoludur.
# List'lerde aynı şekilde verileri tutarlar.

amazon_cart = ["notebooks", "sunglasses"]
print(amazon_cart[1])

# List Slicing - List Dilimleme -> text = "hello" text[0:3:1]

ebay_cart = [
    "toys",
    "grapes",
    "laptop",
    "playstation",
]

# Aynı dizelerde olduğu gibi burada da dizileri dilimleyebiliyoruz.
print(ebay_cart[0:2]) # toys, grapes

# Dizelere yeniden atama yapamıyorduk ancak dizilere (arrays) atama yapabiliyoruz.

ebay_cart[0] = "notebook"
new_cart = ebay_cart[:] # : tüm diziyi kopyalar ve yeni değişkene atar
new_cart[0] = "gum"
print(new_cart)
print(ebay_cart)


