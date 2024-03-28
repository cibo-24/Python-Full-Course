# Scope Rules

a = 1 # global scope

def confusion():
    a = 5
    return a

print(a)
print(confusion())


# Global keywod'ünü kullanmak

total = 0

def count ():
    total = 0
    total += 1
    return total 

print(count())

# Global Keyword, globelde oluşturulmuş değişkeni func içerisinde kullanmaya yarar

total = 10

def counts():
    global total 
    total += 1
    return total

print(counts())

# ya da parametre olarak geçebiliriz

total3 = 20

def count3(total3):
    total3 += 1
    return total3

print(count3(total3))