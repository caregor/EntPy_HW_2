"""
    ---Task 3---
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
"""


def parse_fraction(fraction_str):
    numerator, denominator = fraction_str.split('/')
    return int(numerator), int(denominator)


def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def add_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2

    common_denominator = denominator1 * denominator2

    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1

    sum_numerator = new_numerator1 + new_numerator2

    if is_prime_number(sum_numerator) or is_prime_number(common_denominator):
        divider = nod(sum_numerator, common_denominator)
        sum_numerator = sum_numerator / divider
        common_denominator = common_denominator / divider

    return int(sum_numerator), int(common_denominator)


def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2

    product_numerator = numerator1 * numerator2
    product_denominator = denominator1 * denominator2

    return product_numerator, product_denominator


fraction_str1 = input("Введите первую дробь в формате a/b: ")
fraction_str2 = input("Введите вторую дробь в формате a/b: ")

numerator1, denominator1 = parse_fraction(fraction_str1)
numerator2, denominator2 = parse_fraction(fraction_str2)

sum_result = add_fractions((numerator1, denominator1), (numerator2, denominator2))
multiply_result = multiply_fractions((numerator1, denominator1), (numerator2, denominator2))

# Вывод результатов
print("Сумма дробей:", f"{sum_result[0]}/{sum_result[1]}")
print("Произведение дробей:", f"{multiply_result[0]}/{multiply_result[1]}")
