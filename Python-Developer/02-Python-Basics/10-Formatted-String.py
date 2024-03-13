# formatted String

name = "Johhny"
age = 55

print("hi " + name + ". You are " + str(age)+ " years old")

# Yukarıdakinin farklı ve daha kısa yazılımı NEW VERSİON !!!!
# f başa gelir ve {} içerisine değişken atanır

print (f"hi {name}. You are {age} years old")

# Daha eski bir yöntem .format()
print("hi {0}. You are {1} years old".format(name,age))