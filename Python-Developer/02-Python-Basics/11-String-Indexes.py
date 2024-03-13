# String İndexes

selfish = "me se ck"

print(selfish[0], selfish[7])

# Başlangıç ve bitiş dizesini aynı anda vermek [start:stop]

print(selfish[0:8])

# stepover ile dizi içerisinde ki verilerin üzerinden geçebilirim
# 2 yazarsam, 2şer 2şer atlayarak gezinme yapar

number = "01234567"
print(number[0:8:2])

# başlama değerini ayarlama. 1'den başlar -> nereye kadar gideceğini belirleme. 5. indexe kadar gider
print(number[1:])
print(number[:5])

# Eğer index numarasını negatif yaparsak sondan başlayacaktır.

numberTo = "01234567"
print(numberTo[::-1]) # tersten yazdırma işlemi


# Değişmezlik Kuralı

# Python'da dizileri değiştiremeyiz.

fish = "balık alabalık hamsi"

# fish[0] = "ko" # bu değeri değiştirmek hataya neden olacaktır. İndex yerine ancak değişken değerini tümüyle değiştirebilirim

# Atama yapmak

fish = fish + "çupra"
print(fish)


