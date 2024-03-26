# Docstrings: fonksiyonlarımızın içerisine bilgi vermek amacıyla yazıdğımız yorum satırı. Bu daha sonra bu fonksiyonu çağırdığımızda bilgi satırı olarak geçecektir.

def test(a):
    '''
    Info: Bu fonksiyon test için yazılmıştır.
    '''
    print(a)

test("Kenan")
# fonskiyon bilgilerini göreceğimiz help() veya __doc__ metodu
help(test)
print(test.__doc__)