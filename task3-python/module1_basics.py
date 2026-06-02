# ------------------------------------------------------------
# Карточка сотрудника

print("\n" + "="*50)
print("   Карточка сотрудника")
print("="*50)

# Создание переменных с данными сотрудника
employee_full_name = "Алексей Серов"      # str: полное имя сотрудника
employee_age_years = 23                   # int: возраст в годах
employee_monthly_salary = 87000.90        # float: ежемесячная зарплата в рублях
is_employee_working = True                # bool: статус занятости (работает/не работает)

# Вывод информации в читаемом формате
print("\n" + "-"*50)
print(" Личная информация:")
print("-"*50)
print(f" Имя сотрудника:      {employee_full_name}")
print(f" Возраст:             {employee_age_years} лет")
print(f" Ежемесячная зарплата: {employee_monthly_salary:.2f} ₽")
print(f" Статус занятости:    {'Работает' if is_employee_working else 'Не работает'}")
print("-"*50)
print(f" Итог: Сотрудник {employee_full_name}, {employee_age_years} года, работает в компании")
print("="*50)

# ------------------------------------------------------------
# Exercise 2. Greeting
# Demonstrates: input(), str concatenation, f-string
# ------------------------------------------------------------
# Приветствие сотрудника

print("\n" + "="*50)
print("   Приветствие сотрудника")
print("="*50)

# Запрос данных у пользователя
print("\n" + "="*50)
print("   Приветствие сотрудника")
print("="*50)

# Запрос данных у пользователя
user_name = input("Введите имя сотрудника: ")
user_city = input("Введите город сотрудника: ")

# Вывод приветствия
print("\n" + "-"*50)
print(" Приветствие:")
print("-"*50)
print(f" Сотрудник {user_name} работает в офисе {user_city}")
print("-"*50)
print(f" Рады приветствовать {user_name} из города {user_city}!")
print("="*50)
# ------------------------------------------------------------
# Exercise 3. Order Cost
# Demonstrates: input(), float(), int(), multiplication
# ------------------------------------------------------------
# Калькулятор стоимости заказа (с защитой от ошибок)

print("\n" + "="*50)
print("   Калькулятор стоимости заказа")
print("="*50)

# Функция для безопасного ввода числа
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print(" Число не может быть отрицательным. Попробуйте снова.")
        except ValueError:
            print(" Ошибка: нужно ввести число. Попробуйте снова.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print(" Число не может быть отрицательным. Попробуйте снова.")
        except ValueError:
            print(" Ошибка: нужно ввести целое число. Попробуйте снова.")

# Ввод данных (теперь без ошибок)
product_price = get_float_input(" Введите цену товара (₽):100 ")
product_quantity = get_int_input(" Введите количество товара:10")
# Калькулятор стоимости заказа (с заданными значениями)

print("\n" + "="*50)
print("   Калькулятор стоимости заказа")
print("="*50)

# Заданные значения
product_price = 100        # float: цена товара в рублях
product_quantity = 10      # int: количество товара

# Расчет итоговой стоимости заказа
order_total_cost = product_price * product_quantity

# Вывод результата
print("\n" + "-"*50)
print(" Детали заказа:")
print("-"*50)
print(f" Цена товара:       {product_price:>10.2f} ₽")
print(f" Количество:        {product_quantity:>10} шт.")
print(f" Итоговая стоимость: {order_total_cost:>10.2f} ₽")
print("-"*50)
print(f" Итог: Стоимость заказа = {order_total_cost:.2f} рублей")
print("="*50)

# ------------------------------------------------------------
# Exercise 4. Deposit Income
# Demonstrates: input(), float(), percentage calculation
# ------------------------------------------------------------
# Расчет годового дохода по банковскому вкладу

print("\n" + "="*50)
print("   Расчет годового дохода по вкладу")
print("="*50)

# Ввод данных от пользователя
deposit_amount = float(input(" Введите сумму вклада (в рублях): "))
deposit_interest_rate = float(input(" Введите годовую процентную ставку (%): "))

# Расчет годового процентного дохода
annual_interest_income = deposit_amount * (deposit_interest_rate / 100)

# Вывод результата с пояснениями
print("\n" + "-"*50)
print(" Результат расчета:")
print("-"*50)
print(f" Сумма вклада:          {deposit_amount:>10.2f} ₽")
print(f" Годовая ставка:        {deposit_interest_rate:>10.2f} %")
print(f" Годовой процентный доход: {annual_interest_income:>10.2f} ₽")
print("-"*50)
print(f" Итог: За год ваш вклад вырастет на {annual_interest_income:.2f} рублей")
print("="*50)
# Доход по вкладу (пример с заданными числами)

print("\n" + "="*50)
print("   Расчет дохода по вкладу")
print("="*50)

# Заданные значения
deposit_amount = 10_000_000  # сумма вклада 10 млн рублей
deposit_interest_rate = 17    # годовая ставка 17%

# Расчет годового процентного дохода
annual_interest_income = deposit_amount * (deposit_interest_rate / 100)

# Вывод результата
print("\n" + "-"*50)
print(" Результат расчета:")
print("-"*50)
print(f" Сумма вклада:        {deposit_amount:>12,.2f} ₽")
print(f" Годовая ставка:      {deposit_interest_rate:>12.2f} %")
print(f" Годовой доход:       {annual_interest_income:>12,.2f} ₽")
print("-"*50)
print(f" Итог: За год ваш вклад вырастет на {annual_interest_income:,.2f} рублей")
print(f" Сумма в конце года: {deposit_amount + annual_interest_income:,.2f} ₽")
print("="*50)

==================================================
   Пример.Расчет годового дохода по вкладу
==================================================
 Введите сумму вклада (в рублях): 10000000
 Введите годовую процентную ставку (%): 17

--------------------------------------------------
 Результат расчета:
--------------------------------------------------
 Сумма вклада:              1000000.00 ₽
 Годовая ставка:               17.00 %
 Годовой процентный доход:   1700000.00 ₽
--------------------------------------------------
 Итог: За год ваш вклад вырастет на 1700000.00 рублей
==================================================
# ------------------------------------------------------------
# Exercise 5. Currency Converter (RUB → USD)
# Demonstrates: division, rounding, format specifier
# ------------------------------------------------------------
# Конвертер валют: Рубли → Доллары США

print("\n" + "="*50)
print("   Конвертер валют RUB → USD")
print("="*50)

# Ввод данных от пользователя
usd_exchange_rate = float(input(" Введите курс доллара (₽ за 1 $): "))
rub_amount_to_convert = float(input(" Введите сумму в рублях (₽): "))

# Конвертация рублей в доллары
usd_converted_amount = rub_amount_to_convert / usd_exchange_rate

# Вывод результата (округление до 2 знаков)
print("\n" + "-"*50)
print(" Результат конвертации:")
print("-"*50)
print(f" Сумма в рублях:   {rub_amount_to_convert:>10.2f} ₽")
print(f" Курс USD:         {usd_exchange_rate:>10.2f} ₽")
print(f" Сумма в долларах: {usd_converted_amount:>10.2f} $")
print("-"*50)
print(f" Итог: {rub_amount_to_convert:.2f} ₽ = {usd_converted_amount:.2f} USD")
print("="*50)
==================================================
  Пример. Конвертер валют RUB → USD
==================================================
 Введите курс доллара (₽ за 1 $): 71.55
 Введите сумму в рублях (₽): 10000

--------------------------------------------------
 Результат конвертации:
--------------------------------------------------
 Сумма в рублях:        10000.00 ₽
 Курс USD:                71.55 ₽
 Сумма в долларах:        139.76 $
--------------------------------------------------
Итог: 10000.00 ₽ = 139.76 USD
==================================================

# ------------------------------------------------------------
# Exercise 6. Profit and Profitability
# Demonstrates: subtraction, division, percentage
# ------------------------------------------------------------
# Калькулятор прибыли и рентабельности

# Прибыль и рентабельность (пример с новыми цифрами)

print("\n" + "="*50)
print("   Расчет прибыли и рентабельности")
print("="*50)

# Заданные значения 
company_revenue = 2_500_000      # выручка 2.5 млн рублей
company_costs = 1_850_000        # затраты 1.85 млн рублей

# Расчет прибыли и рентабельности
company_profit = company_revenue - company_costs
profitability_percent = (company_profit / company_revenue) * 100

# Вывод результатов
print("\n" + "-"*50)
print(" Финансовые показатели:")
print("-"*50)
print(f" Выручка:           {company_revenue:>12,.2f} ₽")
print(f" Затраты:           {company_costs:>12,.2f} ₽")
print(f" Прибыль:           {company_profit:>12,.2f} ₽")
print(f" Рентабельность:    {profitability_percent:>11.2f} %")
print("-"*50)

# Анализ результатов
if company_profit > 0:
    print(f" Компания работает с прибылью! +{company_profit:,.2f} ₽")
    if profitability_percent >= 20:
        print(" Отличная рентабельность! (>20%)")
    elif profitability_percent >= 10:
        print(" Хорошая рентабельность (>10%)")
    else:
        print(" Низкая рентабельность, есть куда расти")
elif company_profit < 0:
    print(f" Компания работает в убыток: {company_profit:,.2f} ₽")
else:
    print(" Компания работает в ноль (прибыль = 0)")

print("="*50)
==================================================
   Расчет прибыли и рентабельности
==================================================

--------------------------------------------------
 Финансовые показатели:
--------------------------------------------------
 Выручка:           2,500,000.00 ₽
 Затраты:           1,850,000.00 ₽
 Прибыль:             650,000.00 ₽
 Рентабельность:         26.00 %
--------------------------------------------------
 Компания работает с прибылью! +650,000.00 ₽
 Отличная рентабельность! (>20%)
==================================================
# ------------------------------------------------------------
# Exercise 7. Stock Price Change
# Demonstrates: subtraction, division, multiplication
# ------------------------------------------------------------
# Анализ изменения цены акции

print("\n" + "="*50)
print("   Анализ изменения цены акции")
print("="*50)

# Функция для безопасного ввода чисел
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print(" Цена не может быть отрицательной. Попробуйте снова.")
        except ValueError:
            print(" Ошибка: нужно ввести число. Попробуйте снова.")

# Ввод данных
initial_stock_price = get_float_input("📈 Введите начальную цену акции (₽): ")
final_stock_price = get_float_input("📉 Введите конечную цену акции (₽): ")

# Расчет изменений
absolute_price_change = final_stock_price - initial_stock_price

# Проверка на деление на ноль
if initial_stock_price > 0:
    percentage_price_change = (absolute_price_change / initial_stock_price) * 100
else:
    percentage_price_change = 0.0
    print("\n Внимание: Начальная цена равна 0, процентное изменение невозможно рассчитать.")

# Вывод результатов
print("\n" + "-"*50)
print(" Анализ изменения цены:")
print("-"*50)
print(f" Начальная цена:    {initial_stock_price:>10.2f} ₽")
print(f" Конечная цена:     {final_stock_price:>10.2f} ₽")
print(f" Абсолютное изменение: {absolute_price_change:>10.2f} ₽")
print(f" Процентное изменение: {percentage_price_change:>10.2f} %")
print("-"*50)

# Визуализация изменения
if absolute_price_change > 0:
    print(f" Акция выросла на {absolute_price_change:.2f} ₽ (+{percentage_price_change:.2f}%)")
    print(f"   {'▲' * min(int(abs(percentage_price_change) / 2), 20)}")
elif absolute_price_change < 0:
    print(f" Акция упала на {abs(absolute_price_change):.2f} ₽ ({percentage_price_change:.2f}%)")
    print(f"   {'▼' * min(int(abs(percentage_price_change) / 2), 20)}")
else:
    print("➖ Цена акции не изменилась")
    
print("="*50)
==================================================
   Анализ изменения цены акции
==================================================
 Начальная цена:      1,250,000.00 ₽
 Конечная цена:       1,450,000.00 ₽
 Абсолютное изменение:   200,000.00 ₽
 Процентное изменение:       16.00 %
--------------------------------------------------
 Акция выросла на 200,000.00 ₽ (+16.00%)
==================================================
# ------------------------------------------------------------
# Exercise 8. Mini Price List
# Demonstrates: multiple inputs, string storage, formatted output
# ------------------------------------------------------------
# Мини-прайс-лист: Автомобили

# Мини-прайс-лист: Автомобили (обновлённая версия)

print("\n" + "="*50)
print("   Мини-прайс-лист: АВТОМОБИЛИ")
print("="*50)

# Данные об автомобилях (с Dodge вместо Camry)
first_product_name = "Dodge Challenger SRT Demon 170"
first_product_price = 9_500_000.00

second_product_name = "BMW X5"
second_product_price = 7_920_000.00

third_product_name = "Audi Q7"
third_product_price = 6_450_000.00

# Вывод прайс-листа
print("\n" + "="*50)
print("    ПРАЙС-ЛИСТ АВТОМОБИЛЕЙ")
print("="*50)
print(f"    {first_product_name} — {first_product_price:,.2f} руб.")
print(f"    {second_product_name} — {second_product_price:,.2f} руб.")
print(f"    {third_product_name} — {third_product_price:,.2f} руб.")
print("="*50)

# Статистика
total_sum = first_product_price + second_product_price + third_product_price
average_price = total_sum / 3
max_price = max(first_product_price, second_product_price, third_product_price)
min_price = min(first_product_price, second_product_price, third_product_price)

print("\n Статистика прайс-листа:")
print(f"    Общая стоимость: {total_sum:,.2f} руб.")
print(f"    Средняя цена: {average_price:,.2f} руб.")
print(f"    Самый дорогой: {max_price:,.2f} руб.")
print(f"   Самый дешёвый: {min_price:,.2f} руб.")
print("="*50)

==================================================
    ПРАЙС-ЛИСТ АВТОМОБИЛЕЙ
==================================================
    Dodge Challenger SRT Demon 170 — 9,500,000.00 руб.
    BMW X5 — 7,920,000.00 руб.
    Audi Q7 — 6,450,000.00 руб.
==================================================
 Статистика прайс-листа:
    Общая стоимость: 23,870,000.00 руб.
    Средняя цена: 7,956,666.67 руб.
    Самый дорогой: 9,500,000.00 руб.
    Самый дешёвый: 6,450,000.00 руб.
==================================================
# ------------------------------------------------------------
# Exercise 9. Annual Budget
# Demonstrates: multiplication, subtraction, multi-line output
# ------------------------------------------------------------
# Годовой бюджет

print("\n" + "="*50)
print("   Расчет годового бюджета")
print("="*50)

#  цифры
monthly_income = 150_000      # ежемесячный доход 150 000 ₽
monthly_expenses = 95_000     # ежемесячные расходы 95 000 ₽

# Расчет годовых сумм
annual_income_total = monthly_income * 12
annual_expenses_total = monthly_expenses * 12
annual_balance_total = annual_income_total - annual_expenses_total

# Вывод результатов (только 3 строки по заданию)
print(f"Годовой доход: {annual_income_total:.2f} RUB")
print(f"Годовые расходы: {annual_expenses_total:.2f} RUB")
print(f"Годовой остаток: {annual_balance_total:.2f} RUB")
==================================================
   Расчет годового бюджета
==================================================
Годовой доход: 1800000.00 RUB
Годовые расходы: 1140000.00 RUB
Годовой остаток: 660000.00 RUB
# ------------------------------------------------------------
# Exercise 10. Invoice with VAT
# Demonstrates: VAT calculation, percentage, multi-step calculation
# ------------------------------------------------------------
# Счёт с НДС
# Программа для расчёта стоимости товара с учётом налога на добавленную стоимость

# Счёт с НДС (пример с новыми числами)

print("\n" + "="*50)
print("   Счёт с НДС")
print("="*50)

# Ввод данных (с другими числами)
product_quantity_vat = int(input(" Введите количество товара: "))
product_unit_price = float(input(" Введите цену за единицу (₽): "))
vat_percent = float(input("🧾 Введите ставку НДС (%): "))

# Расчёт
subtotal_without_vat = product_quantity_vat * product_unit_price
vat_amount = subtotal_without_vat * (vat_percent / 100)
total_with_vat = subtotal_without_vat + vat_amount

# Вывод счёта
print("\n" + "="*50)
print("    СЧЁТ")
print("="*50)
print(f"   Количество товара:      {product_quantity_vat} шт.")
print(f"   Цена за единицу:        {product_unit_price:>10.2f} ₽")
print("-"*50)
print(f"   Стоимость без НДС:      {subtotal_without_vat:>10.2f} ₽")
print(f"   Сумма НДС ({vat_percent:.0f}%):      {vat_amount:>10.2f} ₽")
print("-"*50)
print(f"   ИТОГО с НДС:           {total_with_vat:>10.2f} ₽")
print("="*50)

# Дополнительная информация
print("\n Налоговая информация:")
if vat_percent == 20:
    print("   • Основная ставка НДС (20%)")
elif vat_percent == 10:
    print("   • Пониженная ставка НДС (10%)")
elif vat_percent == 0:
    print("   • Нулевая ставка НДС")
else:
    print(f"   • Специальная ставка НДС ({vat_percent:.0f}%)")
print(f"   • Сумма налога к уплате: {vat_amount:,.2f} ₽")
print("="*50)
# 1. Стоимость без НДС
subtotal_without_vat = product_quantity_vat * product_unit_price

# 2. Сумма НДС
vat_amount = subtotal_without_vat * (vat_percent / 100)

# 3. Итого с НДС
total_with_vat = subtotal_without_vat + vat_amount
==================================================
   Пример.Счёт с НДС
==================================================
 Введите количество товара: 15
 Введите цену за единицу (₽): 1200
 Введите ставку НДС (%): 20

==================================================
    СЧЁТ
==================================================
   Количество товара:      15 шт.
   Цена за единицу:          1200.00 ₽
--------------------------------------------------
   Стоимость без НДС:       18000.00 ₽
   Сумма НДС (20%):          3600.00 ₽
--------------------------------------------------
   ИТОГО с НДС:             21600.00 ₽
==================================================

  Налоговая информация:
   • Основная ставка НДС (20%)
   • Сумма налога к уплате: 3,600.00 ₽
==================================================
