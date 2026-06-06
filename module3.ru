День 9. Модуль 3. Функции → module3_functions.py
Что нужно освоить: def, параметры, return. Выполнить любые 5 упражнений из списка ниже.


"""

from typing import List, Tuple, Union, Optional

# ===================== 1. calculate_profit =====================
def calculate_profit(revenue: float, costs: float) -> float:
    """
    Рассчитывает прибыль как разницу между выручкой и затратами.

    Параметры:
        revenue (float): Выручка (должна быть >= 0)
        costs (float): Затраты (должны быть >= 0)

    Возвращает:
        float: Прибыль (может быть отрицательной)
    """
    if revenue < 0 or costs < 0:
        raise ValueError("Выручка и затраты не могут быть отрицательными")
    return revenue - costs

# Примеры вызова
print("=== 1. Прибыль ===")
print(f"Прибыль (200, 150): {calculate_profit(200, 150)}")
print(f"Прибыль (500, 600): {calculate_profit(500, 600)}")
print(f"Прибыль (0, 50):   {calculate_profit(0, 50)}")

# ===================== 2. calculate_vat =====================
def calculate_vat(price: float, vat_rate: float = 20.0) -> float:
    """
    Вычисляет сумму НДС от цены.

    Параметры:
        price (float): Цена товара
        vat_rate (float): Ставка НДС в процентах (по умолчанию 20%)

    Возвращает:
        float: Сумма налога
    """
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    return price * vat_rate / 100

print("\n=== 2. НДС ===")
print(f"НДС (5000 руб, ставка 20% по умолчанию): {calculate_vat(5000)} руб")
print(f"НДС (700 руб, ставка 10% явно): {calculate_vat(700, 10)} руб")

# ===================== 3. get_category =====================
def get_category(revenue: float) -> str:
    """
    Определяет категорию бизнеса по годовой выручке.

    Категории:
        - микро: до 5 млн руб
        - малый: 5–100 млн руб
        - средний: 100–1 млрд руб
        - крупный: более 1 млрд руб

    Параметры:
        revenue (float): Годовая выручка

    Возвращает:
        str: Категория бизнеса
    """
    if revenue < 0:
        return "некорректная выручка"
    if revenue < 1_000_000:
        return "микро"
    elif revenue < 100_000_000:
        return "малый"
    elif revenue < 1_000_000_000:
        return "средний"
    else: 
        return "крупный"
      
      
print("\n=== 3. Категория бизнеса ===")
test_revenues = [1_500_000, 50_000_000, 500_000_000, 3_000_000_000]
for rev in test_revenues:
    print(f"Выручка {rev:>12,} руб → категория: {get_category(rev)}")

# ===================== 4. compound_interest =====================
def compound_interest(capital: float, rate: float, years: int) -> float:
    """
    Рассчитывает итоговую сумму по формуле сложных процентов.

    Параметры:
        capital (float): Начальный капитал
        rate (float): Годовая процентная ставка (в процентах)
        years (int): Количество лет

    Возвращает:
        float: Итоговая сумма
    """
    if capital < 0 or rate < 0 or years < 0:
        raise ValueError("Все параметры должны быть неотрицательными")
    return capital * (1 + rate / 100) ** years

print("\n=== 4. Сложные проценты ===")
capital = 100_000
rate = 8
for years in [3, 5, 10]:
    total = compound_interest(capital, rate, years)
    print(f"{capital} руб под {rate}% на {years} лет → {total:,.2f} руб")

# ===================== 5. apply_discount =====================
def apply_discount(price: float, discount_percent: float) -> float:
    """
    Применяет скидку к цене и возвращает новую цену.

    Параметры:
        price (float): Исходная цена
        discount_percent (float): Процент скидки (0–100)

    Возвращает:
        float: Цена со скидкой
    """
    if not (0 <= discount_percent <= 100):
        raise ValueError("Скидка должна быть от 0 до 100")
    return price * (100 - discount_percent) / 100

print("\n=== 5. Скидки на товары ===")
products = [
    {"name": "Ноутбук", "price": 60_000, "discount": 10},
    {"name": "Мышь", "price": 1_200, "discount": 5},
    {"name": "Клавиатура", "price": 3_500, "discount": 15},
    {"name": "Монитор", "price": 22_000, "discount": 20},
  список, в реальной работе вызвали бы get_revenues(3)
sample_revenues = [120_000, 95_000, 150_000]
print(f"Список выручки: {sample_revenues}")
min_val, max_val, mean_val = analyze(sample_revenues)
print(f"Минимум: {min_val:.2f}, Максимум: {max_val:.2f}, Среднее: {mean_val:.2f}")

# ===================== 6. currency_convert =====================
def currency_convert(amount: float, rate: float, direction: str = "to_rub") -> float:
    """
    Конвертирует валюту по заданному курсу.

    Параметры:
        amount (float): Сумма для конвертации
        rate (float): Курс (например, 90 руб за USD)
        direction (str): 'to_rub' (из USD в RUB) или 'to_usd' (из RUB в USD)

    Возвращает:
        float: Конвертированная сумма
    """
    if amount < 0 or rate <= 0:
        raise ValueError("Сумма и курс должны быть положительными")
    if direction == "to_rub":
        return amount * rate
    elif direction == "to_usd":
        return amount / rate
    else:
        raise ValueError("Направление должно быть 'to_usd' или 'to_rub'")

print("\n=== 6. Конвертация валют ===")
usd_amount = 100
rub_amount = 9000
exchange_rate = 90.5

print(f"100 USD → RUB (курс {exchange_rate}): {currency_convert(usd_amount, exchange_rate, 'to_rub'):.2f} руб")
print(f"9000 RUB → USD (курс {exchange_rate}): {currency_convert(rub_amount, exchange_rate, 'to_usd'):.2f} USD")

# ===================== 7. payback_period =====================
def payback_period(investment: float, annual_profit: float) -> Union[float, str]:
    """
    Рассчитывает срок окупаемости инвестиций (в годах).

    Параметры:
        investment (float): Объём инвестиций
        annual_profit (float): Годовая прибыль

    Возвращает:
        float: Количество лет окупаемости
        str: Сообщение об ошибке, если прибыль ≤ 0
    """
    if annual_profit <= 0:
        return "Окупаемости нет (прибыль ≤ 0)"
    return investment / annual_profit

print("\n=== 7. Окупаемость ===")
print(f"Инвестиции 1_000_000, прибыль 200_000/год → {payback_period(1_000_000, 200_000):.2f} лет")
print(f"Инвестиции 500_000, прибыль 0 → {payback_period(500_000, 0)}")

# ===================== 8. format_invoice_line =====================
def format_invoice_line(name: str, quantity: float, price: float) -> str:
    """
    Формирует строку для строки счёта.

    Параметры:
        name (str): Название товара/услуги
        quantity (float): Количество
        price (float): Цена за единицу

    Возвращает:
        str: Отформатированная строка
    """
    total = quantity * price
    return f"{name} × {quantity} = {total:.2f} руб"

print("\n=== 8. Строки счёта ===")
invoice_items = [
    ("Ручка синяя", 10, 15.5),
    ("Блокнот А5", 3, 89.0),
    ("Степлер", 1, 245.0),
]
for name, qty, pr in invoice_items:
    print(format_invoice_line(name, qty, pr))

# ===================== 9. get_revenues + analyze =====================
def get_revenues(n: int) -> List[float]:
    """
    Запрашивает у пользователя n значений выручки и возвращает их списком.

    Параметры:
        n (int): Количество значений

    Возвращает:
        List[float]: Список введённых значений
    """
    revenues = []
    for i in range(1, n + 1):
        while True:
            try:
                val = float(input(f"Введите выручку за период {i}: "))
                revenues.append(val)
                break
            except ValueError:
                print("Ошибка: введите число")
    return revenues

def analyze(values: List[float]) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    """
    Принимает список чисел и возвращает минимум, максимум и среднее.

    Параметры:
        values (List[float]): Список чисел

    Возвращает:
        Tuple[Optional[float], Optional[float], Optional[float]]: (min, max, mean)
        Если список пуст, возвращает (None, None, None)
    """
    if not values:
        return None, None, None
    return min(values), max(values), sum(values) / len(values)

print("\n=== 9. Ввод и анализ выручки ===")
print("(Для демонстрации введём 3 значения программно, замените на input() при интерактиве)")
# Для автоматической демонстрации создаём список, в реальной работе вызвали бы get_revenues(3)
sample_revenues = [120_000, 95_000, 150_000]
print(f"Список выручки: {sample_revenues}")
min_val, max_val, mean_val = analyze(sample_revenues)
print(f"Минимум: {min_val:.2f}, Максимум: {max_val:.2f}, Среднее: {mean_val:.2f}")

# ===================== 10. generate_report =====================
def generate_report(company_name: str, revenue: float, costs: float) -> None:
    """
    Генерирует и выводит многострочный финансовый отчёт.

    Параметры:
        company_name (str): Название компании
        revenue (float): Выручка
        costs (float): Затраты
    """
    profit = revenue - costs
    # Избегаем деления на ноль для рентабельности
    if revenue > 0:
        profitability = (profit / revenue) * 100
    else:
        profitability = float('nan')  # не определено

    status = "прибыльна" if profit > 0 else "убыточна" if profit < 0 else "нулевая"

    # Формируем отчёт
    report = f"""
    ╔══════════════════════════════════════╗
    ║        ФИНАНСОВЫЙ ОТЧЁТ             ║
    ╠══════════════════════════════════════╣
    ║ Компания: {company_name:<28} ║
    ║ Выручка: {revenue:>28,.2f} руб ║
    ║ Затраты: {costs:>28,.2f} руб ║
    ║ Прибыль: {profit:>28,.2f} руб ║
    ║ Рентабельность: {profitability:>18.2f} % ║
    ║ Статус: {status:>30} ║
    ╚══════════════════════════════════════╝
    """
    print(report)

print("\n=== 10. Генерация отчёта ===")
generate_report("ООО 'Парус'", revenue=2_500_000, costs=1_800_000)
generate_report("ИП 'Иванов'", revenue=500_000, costs=750_000)
generate_report("Новая компания", revenue=1_000_000, costs=1_000_000)
