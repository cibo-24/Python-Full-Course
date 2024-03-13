# Ternary Operator
# condition_if_true if condition else condition_if_else

is_friend = True
# Eğer is_friend true ise "message allowed" değil ise else bloğunu çalıştır.
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)


is_number = 40
age = 25
last_name = "Cibooglu" if is_number else age
print(last_name)