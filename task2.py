"""
    ---Task 2---
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def decimal_to_hexadecimal(decimal):
    result = ""
    if decimal == 0:
        result = "0"
    else:
        hex_chars = "0123456789ABCDEF"
        while decimal > 0:
            remainder = decimal % 16
            result = hex_chars[remainder] + result
            decimal = decimal // 16
    return '0x' + result


number = int(input("Введите целое число: "))

hexadecimal = decimal_to_hexadecimal(number)

print("Шестнадцатеричное представление числа:", hexadecimal)
print("Проверка: hex =", hex(number))
