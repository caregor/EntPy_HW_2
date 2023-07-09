"""
    ---Task 1---
Задание No6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""


def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    fee = max(fee, 30)
    fee = min(fee, 600)
    return fee


def calculate_tax(amount):
    tax = amount * 0.1
    return tax


balance = 0
operations_count = 0

while True:
    print("Текущий баланс:", balance)

    action = input("Выберите действие:\n - 1 -- пополнить;\n - 2 -- снять;\n - 3 -- выйти;\n")

    if action == '1':
        deposit = int(input("Введите сумму для пополнения (кратно 50): "))
        if deposit % 50 == 0:
            balance += deposit
            operations_count += 1
            if operations_count % 3 == 0:
                interest = balance * 0.03
                balance += interest
        else:
            print("Ошибка: Сумма пополнения должна быть кратна 50.")

    elif action == '2':
        withdrawal = int(input("Введите сумму для снятия (кратно 50): "))
        if withdrawal % 50 == 0:
            if withdrawal <= balance:
                fee = calculate_withdrawal_fee(withdrawal)
                print("Комиссия за операцию:", fee)
                balance -= withdrawal
                balance -= fee
                operations_count += 1
                if operations_count % 3 == 0:
                    interest = balance * 0.03
                    print("Начисление за лояльность к банку:", interest)
                    balance += interest
            else:
                print("Ошибка: Недостаточно средств на счете.")
        else:
            print("Ошибка: Сумма снятия должна быть кратна 50.")

    elif action == '3':
        if balance > 5000000:
            tax = calculate_tax(balance)
            balance -= tax
            print("Удержан налог на богатсво 10%")
        break

    else:
        print("Ошибка: Неверное действие.")

print("Баланс:", balance)
