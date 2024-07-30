
# print('Введите длину стороны квадрата')
# square = int(input())
# b = square**2
# print('Площадь квадрата с заданной стороной =', b)


from math import ceil

def square(a):
    s = a ** 2
    return s

a = float(input("Длина стороны квадрата: "))
result = square(a)
rounded_result = ceil(result)
print(f'Округленная в большую сторону сумма - {rounded_result}')