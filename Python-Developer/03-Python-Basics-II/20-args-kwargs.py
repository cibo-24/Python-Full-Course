# *args - **kwargs

# bu fonksiyon tek bir argüman aldığı için hata verecektir. Bunun için *args kullanmalıyız.

def super_func(args):
    return sum(args)

# sum(), toplama işlemi yapacaktır.
# birden çok argümana sahip olmak için *args kullanmalıyız.

def super_func2(*args):
    return sum(args)
print(super_func2(1,2,3,4))

def super(*hoo):
    return sum(hoo)
print(super(5,10))

# **kwargs
# bu metod ile fazladan argümanlar ekleyebiliriz. Buda fazladan değişken anlamına gelir.

def func_super(*args, **kwargs):
    print(kwargs)
    return sum(args)
print(func_super(1,2,3,4,5, num1=5, num2=10))

# argümanları birbiri ile toplayalım.
def sumFunc(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(sumFunc(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
