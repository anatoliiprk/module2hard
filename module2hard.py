print('Задание "Слишком древний шифр')
def get_password(n):
    if n < 3 or n > 20:
        return 'Число из первой вставки введено неверно'
    else:
        result = ('')
        for i in range(1, n):
            for j in range(1, n):
                a = i + j
                if j > i and n % a == 0:
                    result += str(i)
                    result += str(j)
                else:
                    continue
        str(result)
        return result
number = int(input('Введите число из первой вставки: '))
password = get_password(number)
print('Необходимый пароль: ', password)
