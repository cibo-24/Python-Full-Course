# break-continue-pass
# break aynı zamanda for loops'dada kullanılabilir.

my_list = [1,2,3]
for item in my_list:
    print(item)
    continue
    print("hello for")

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
    print("hello while")

# continue'dan sonrasını görmez. Çünkü continue keywords'ü döngünün başını döndürür
# pass hiçbir işe yaramaz