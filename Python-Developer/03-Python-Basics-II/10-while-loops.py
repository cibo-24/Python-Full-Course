# while Loops
# while loops, sürekli döngüde olmasını sağlar.
# ancak "break" keyword'ü ile birlikte while loops'u durdururuz.

i = 0
while i < 50:
    print(i)
    break

# i'yi 40'a kadar yazdırmak
while i < 40:
    print(i)
    i = i + 1

# while loops ile else'de kullanabiliriz
while i < 30:
    print(i)
    break
else:
    print("done with all the work")

# ne zaman for loops ne zaman while kullanmalıyım
# ne kadar döngü kullanacağımızı bilmediğimiz zaman while kullanmak daha iyi iyidir.
    
while True:
    response = input("say something: ")
    if (response == "bye"):
        break

