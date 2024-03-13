# Password Checker

# Kullanıcıdan iki input değeri alacağımız ve bunu print ile ekrana yazdıracağımz bir password checker.

#Kullanıcı adını daha sonra 6 harf uzunluğunda bir password istenecektir.
# Password güvenlikten dolayı gözükmeyecektir. print("*" * 10) -> **********

names = input("Hello there, what's your name?:")
password = input("Password please!:")

password_length = len(password) # password uzunluğunu almak
hidden_password = "*" * password_length


print(f"Helllo Humans, this is your name {names}, your password {hidden_password} is {password_length} letters long ")




