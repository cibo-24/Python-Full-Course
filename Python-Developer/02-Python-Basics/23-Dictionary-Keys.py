# Bir list'in anahtarlarının değiştirilmemesi beklenir. Çünkü her anahtar-değer çifti bellekte saklanır.
# Ve anahtarlar benzersiz adlara sahip olmalıdır.


dictionary = {
    123: [1,2,3],
    'greeting': 'hello',
    'is_Magic': True,
}

print(dictionary[123])

