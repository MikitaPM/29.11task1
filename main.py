def secret():
    a = input('Введите номер карты')
    b = "**** **** **** "
    с= b+a[12:]
    print("Скрытый  номер: ", с)
s = secret()
print(s)
