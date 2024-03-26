# Short Circuiting

is_Friend = True
is_User = True

# ifadelerden ikisininde true olması durumunda print basılır.
if is_Friend and is_User:
    print("Merhaba dostum!")

# ifadelerden birisi doğru olsada print basılır.
if is_Friend or is_User:
    print("Sadece sen varsın!")