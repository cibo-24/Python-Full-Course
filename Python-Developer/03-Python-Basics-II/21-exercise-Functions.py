# list içerisinde ki en yüksek çift sayıyı basan bir func oluşturalım.

# evens list'in içerisine append metodu ile items içerisinde kileri koyduk.
# max() ile en büyük çift sayıyı bulduk

def highest_even(li):
    evens = []
    for items in li:
        if items % 2 == 0:
           evens.append(items)
    return max(evens)
       
print(highest_even([10,2,3,4,8,11]))