# enumerate() metodu

# enumerate() içerisine yazdığımıza göre index numarasını verir.
# eğer bir index numarasına ihtiyacımız varsa kullanılabilir.
for char in enumerate("helooo"):
    print(char)

# list içerisinde bir range ile oluşturulmuş sayı dizisinde, 50. indexte ne var onu bulmamız gerekiyor.
# i = index
# f, hem number hem string basmamızı sağlar.
for i, item in enumerate(list(range(100))):
    if item == 50:
        print(f"index of 50 is: {i}")