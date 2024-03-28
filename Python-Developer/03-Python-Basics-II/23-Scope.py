# Scope - hangi değişenlere sahibim ve hangilerine erişimim var ? 

if True:
    x = 10

def some_func():
    total = 100
    
print(total)
print(x)

# bir fonksiyon içerisinde ki veriye erişmemiz için onun globalde tanımlı olması gerekir.