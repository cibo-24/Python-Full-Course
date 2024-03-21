# Return
# return keywordü, değer döndürmeye yarar. İstediğimiz değeri iade ederde diyebiliriz.

def sum(num1, num2):
   print("hiii")
   return num1 + num2

print(sum(4,5))

# Fonksiyon bir şeyi iyi yapmalıdır.
# Fonksiyon genelde bir şey döndürmelidir.

def sum2(num1, num2):
   return num1 + num2 

total = sum(4,5)
print(sum(10,total))
print(sum(10,sum(4,5)))

# İç İçe Fonksiyonlar

def sum3(num1, num2):
  def another_func(num3, num4):
    return num3 + num4
  return another_func(num1, num2)

total = sum(10,20)
print(total)

