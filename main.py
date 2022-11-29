def secret():
    a = input('Введите номер карты')
    b = "**** **** **** "
    if a == 16:
        с= b+a[12:]
    else:
        print('Такой карты не существует')
    print("Скрытый  номер: ", с)
s = secret()
print(s)
