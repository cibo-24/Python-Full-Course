# Common List Patterns

basket = ["a","x","b","c","d","e","d"]
basket.sort()
basket.reverse() # liste öğelerini tersine çevirir.
print(basket[::-1]) # liste öğelerini düzene sokar. Sıralama yapar yani. Bu yeni bir list oluşturur. basket'i printlersek eski halini basacaktır.

# range, aralık arasına girilen değerleri oluşturur.
print(list(range(1,100)))


# .join() -> iterable

# .join(), yeni bir dizi oluşturur. Var olan dizinin üzerine veri ekler. Eski dizi öğeleri, yeni .join() ile oluşturulmuş verilerden sonra gelir.
sentence = "!"
new_sentence = sentence.join(["hi","my","name's","kenan"])
print(new_sentence)
