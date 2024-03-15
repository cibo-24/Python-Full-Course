# Exercise
# list içerisinde ki öğelerden tekrar edenleri konsola list olarak aktaralım.
some_list = ["a","b","c","b","d","m","n","n"]

repeat = []
for value in some_list:
    if some_list.count(value) > 1:
        repeat.append(value)

print(repeat)