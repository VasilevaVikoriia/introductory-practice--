# ========== ЗАДАНИЕ 1 ==========
def calculate_profit(revenue, costs):
    """
    Функция расчёта прибыли.
    
    ПАРАМЕТРЫ:
        revenue (float): выручка (доход) в рублях
        costs (float): затраты (расходы) в рублях
    
    ВОЗВРАЩАЕТ:
        float: прибыль = выручка - затраты
               положительное число = прибыль
               отрицательное число = убыток
               ноль = безубыточность
    
    ПРИМЕР:
        calculate_profit(100000, 80000) → 20000
    """
    return revenue - costs  # Простая формула прибыли


    """
    Тестирование функции calculate_profit().
    Используются заданные числа: 10000, 40000, 20000, 15000, 150000.
    """
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 1: Расчёт прибыли")
    print("=" * 60)
    
    # Список пар (выручка, затраты) с указанными числами
    test_data = [
        (10000, 40000),   # случай 1: затраты больше выручки → убыток
        (20000, 15000),   # случай 2: выручка больше затрат → прибыль
        (150000, 10000)   # случай 3: большая выручка, маленькие затраты
    ]
    
    print("Результаты расчёта прибыли:")
    print("-" * 40)
    
    for revenue, costs in test_data:
        profit = calculate_profit(revenue, costs)
        
        # Форматированный вывод с условиями для наглядности
        print(f"Выручка: {revenue:8,.0f} руб. | Затраты: {costs:8,.0f} руб. → ", end="")
        
        if profit > 0:
            print(f"ПРИБЫЛЬ: {profit:8,.0f} руб. ")
        elif profit < 0:
            print(f"УБЫТОК:  {profit:8,.0f} руб. ")
        else:
            print(f"БЕЗУБЫТОЧНОСТЬ: 0 руб. ")

# ========== ЗАДАНИЕ 2 ==========
def calculate_vat(price, rate=20):
    """
    Расчёт суммы НДС (налога на добавленную стоимость).
    
    ПАРАМЕТРЫ:
        price (float): цена товара без НДС
        rate (float): ставка НДС в процентах (по умолчанию 20%)
    
    ВОЗВРАЩАЕТ:
        float: сумма налога
    
    ПРИМЕРЫ:
        calculate_vat(1000)        → 200.0   (20% по умолчанию)
        calculate_vat(1000, 10)    → 100.0   (10% явно)
    """
    return price * rate / 100

def test_task2():
    """Тестирование calculate_vat с разными ставками (новые числа: 7500 руб)."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 2: Расчёт НДС")
    print("=" * 60)
    
    product_price = 7500  
    print(f"Цена товара: {product_price} руб.")
    print("-" * 40)
    
    # Стандартная ставка 20%
    print(f"НДС 20% (стандарт):     {calculate_vat(product_price):.2f} руб.")
    
    # Пониженная ставка 10% (продовольствие, детские товары)
    print(f"НДС 10% (льготный):     {calculate_vat(product_price, 10):.2f} руб.")
    
    # Нулевая ставка 0% (экспорт)
    print(f"НДС 0% (экспорт):       {calculate_vat(product_price, 0):.2f} руб.")
    
    # Повышенная ставка 25% (тестовый сценарий)
    print(f"НДС 25% (тестовый):     {calculate_vat(product_price, 25):.2f} руб.")

# ========== ЗАДАНИЕ 3 ==========
def get_category(revenue):
    """
    Определение категории бизнеса по годовой выручке.
    
    ПАРАМЕТРЫ:
        revenue (float): годовая выручка в рублях
    
    ВОЗВРАЩАЕТ:
        str: категория бизнеса
    
    КАТЕГОРИИ (НОВЫЕ ГРАНИЦЫ):
        Микробизнес:   до 5 млн руб.
        Малый бизнес:  5 – 25 млн руб.
        Средний бизнес: 25 – 300 млн руб.
        Крупный бизнес: выше 300 млн руб.
    """
    if revenue < 5_000_000:      # до 5 миллионов
        return "Микробизнес"
    elif revenue < 25_000_000:    # 5–25 миллионов
        return "Малый бизнес"
    elif revenue < 300_000_000:   # 25–300 миллионов
        return "Средний бизнес"
    else:                          # выше 300 миллионов
        return "Крупный бизнес"

def test_task3():
    """Тестирование get_category на 4 новых значениях."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 3: Категория бизнеса")
    print("=" * 60)


enues = [
        2_500_000,      # 2.5 млн → Микробизнес
        15_000_000,     # 15 млн  → Малый бизнес
        150_000_000,    # 150 млн → Средний бизнес
        450_000_000     # 450 млн → Крупный бизнес
    ]
    
    print("Категории при разной выручке:")
    print("-" * 40)
    
    for rev in revenues:
        category = get_category(rev)
        # Форматируем выручку с разделителями тысяч
        print(f"Выручка {rev:12,.0f} руб. → {category}")

# ========== ЗАДАНИЕ 4 ==========
def compound_interest(capital, rate_percent, years):
    """
    Расчёт сложного процента (процент на процент).
    
    ПАРАМЕТРЫ:
        capital (float): начальный капитал
        rate_percent (float): годовая процентная ставка (%)
        years (int): срок вклада в годах
    
    ВОЗВРАЩАЕТ:
        float: итоговая сумма через указанное количество лет
    
    ФОРМУЛА: capital × (1 + rate/100)^years
    
    ПРИМЕР:
        compound_interest(100000, 10, 3) → 133100.0
    """
    rate = rate_percent / 100      # Превращаем проценты в десятичную дробь
    return capital * (1 + rate) ** years   # ** years = возведение в степень

def test_task4():
    """Тестирование сложного процента с новыми числами."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 4: Сложный процент (капитализация)")
    print("=" * 60)
    
    # НОВЫЕ ЧИСЛА
    capital = 250_000           # 250 000 рублей
    rate = 12.5                 # 12.5% годовых
    years_list = [2, 4, 6]      # 2, 4 и 6 лет (вместо старых 3,5,10)
    
    print(f"Начальный капитал: {capital:,.0f} руб.")
    print(f"Годовая ставка:    {rate}%")
    print("-" * 40)
    
    for years in years_list:
        result = compound_interest(capital, rate, years)
        print(f"Через {years} год(а/лет): {result:15,.2f} руб.")

# ========== ЗАДАНИЕ 5 ==========
def apply_discount(price, discount_percent):
    """
    Применяет скидку к цене товара.
    
    ПАРАМЕТРЫ:
        price (float): исходная цена
        discount_percent (float): размер скидки в процентах
    
    ВОЗВРАЩАЕТ:
        float: цена со скидкой
    
    ФОРМУЛА: price × (100 - discount_percent) / 100
    """
    return price * (100 - discount_percent) / 100

def test_task5():
    """Применяем скидку 20% к новому списку из 5 товаров."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 5: Скидки на товары")
    print("=" * 60)
    
    # НОВЫЙ список товаров (название, цена)
    products = [
        ("Смартфон", 45_000),      # 45 000 руб.
        ("Чехол", 1_800),          # 1 800 руб.
        ("Зарядное устройство", 3_200),   # 3 200 руб.
        ("Наушники", 12_500),      # 12 500 руб.
        ("Защитное стекло", 950)   # 950 руб.
    ]
    
    discount = 20   # НОВАЯ скидка: 20% (было 15%)
    print(f"Акция: скидка {discount}% на все товары!")
    print("-" * 40)
    
    for name, price in products:
        new_price = apply_discount(price, discount)
        # Экономия = старая цена - новая цена
        savings = price - new_price
        print(f"{name:20} | {price:8,.0f} руб. → {new_price:8,.2f} руб. (экономия {savings:6,.2f} руб.)")

# ========== ЗАДАНИЕ 6 ==========
def currency_convert(amount, rate, direction='to_usd'):
    """
    Конвертация валют (рубли ↔ доллары).
    
    ПАРАМЕТРЫ:
        amount (float): конвертируемая сумма
        rate (float): курс (сколько рублей стоит 1 доллар)
        direction (str): направление конвертации
            'to_usd' - рубли → доллары (деление на курс)
            'to_rub' - доллары → рубли (умножение на курс)
    
    ВОЗВРАЩАЕТ:
        float: сконвертированная сумма
    """
    if direction == 'to_usd':
        return amount / rate        # Рубли → Доллары
    elif direction == 'to_rub':
        return amount * rate        # Доллары → Рубли
    else:
        # Если передано неправильное направление
        raise ValueError("Направление должно быть 'to_usd' или 'to_rub'")

def test_task6():
    """Тестирование конвертации с новым курсом и суммами."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 6: Конвертация валют")
    print("=" * 60)
    
    # НОВЫЙ курс: 96.30 рублей за доллар
  
  usd_rate = 96.30
    
    # НОВЫЕ суммы
    rub_amount = 15_000    # 15 000 рублей
    usd_amount = 250       # 250 долларов
    
    print(f"Курс: 1 USD = {usd_rate} RUB")
    print("-" * 40)
    
    # Конвертация рублей в доллары
    converted_to_usd = currency_convert(rub_amount, usd_rate, 'to_usd')
    print(f"{rub_amount:10,.0f} RUB → {converted_to_usd:8,.2f} USD")
    
    # Конвертация долларов в рубли
    converted_to_rub = currency_convert(usd_amount, usd_rate, 'to_rub')
    print(f"{usd_amount:10,.0f} USD → {converted_to_rub:8,.2f} RUB")
    
    # Дополнительный пример: 5000 рублей
    print(f"5 000 RUB → {currency_convert(5000, usd_rate, 'to_usd'):.2f} USD")

# ========== ЗАДАНИЕ 7 ==========
def payback_period(investment, annual_profit):
    """
    Расчёт срока окупаемости инвестиций.
    
    ПАРАМЕТРЫ:
        investment (float): объём инвестиций (сколько вложили)
        annual_profit (float): годовая прибыль
    
    ВОЗВРАЩАЕТ:
        float: срок окупаемости в годах
        float('inf'): бесконечность, если прибыль ≤ 0 (никогда не окупится)
    
    ФОРМУЛА: инвестиции / годовая прибыль
    """
    if annual_profit <= 0:
        return float('inf')   # inf = бесконечность (не окупится никогда)
    return investment / annual_profit

def test_task7():
    """Тестирование срока окупаемости на новых числах."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 7: Срок окупаемости инвестиций")
    print("=" * 60)
    
    # НОВЫЕ числа: инвестиции 850 000 рублей
    investment = 850_000
    
    # НОВЫЕ сценарии годовой прибыли
    profits = [425_000, 170_000, -30_000, 0]
    
    print(f"Инвестиции: {investment:10,.0f} руб.")
    print("-" * 40)
    
    for profit in profits:
        period = payback_period(investment, profit)
        
        if period == float('inf'):
            # Если прибыль ≤ 0
            if profit < 0:
                print(f"Прибыль {profit:10,.0f} руб. → УБЫТОК, окупаемости НЕТ ")
            else:
                print(f"Прибыль {profit:10,.0f} руб. → НУЛЕВАЯ прибыль, окупаемости НЕТ ")
        else:
            print(f"Прибыль {profit:10,.0f} руб. → окупаемость: {period:.1f} лет ")

# ========== ЗАДАНИЕ 8 ==========
def format_invoice_line(name, quantity, price):
    """
    Форматирует строку для счёта/инвойса.
    
    ПАРАМЕТРЫ:
        name (str): название товара/услуги
        quantity (float): количество
        price (float): цена за единицу
    
    ВОЗВРАЩАЕТ:
        str: отформатированная строка вида "Название × Кол-во = Сумма руб."
    
    ПРИМЕР:
        format_invoice_line("Кофе", 2, 150) → "Кофе × 2 = 300.00 руб."
    """
    total = quantity * price
    return f"{name} × {quantity} = {total:.2f} руб."

def test_task8():
    """Форматирование 3 новых позиций для счёта."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 8: Форматирование счёта (инвойс)")
    print("=" * 60)
    
    # НОВЫЕ позиции (название, количество, цена)
    invoice_items = [
        ("Бизнес-ланч", 5, 420),      # 5 бизнес-ланчей по 420 руб.
        ("Питьевая вода", 12, 65),    # 12 бутылок по 65 руб.
        ("Переговорная комната", 2, 2500)  # 2 часа по 2500 руб.
    ]
    
    print("СЧЁТ №324-Ф:")
    print("-" * 40)
    
    total_invoice = 0
    for name, qty, price in invoice_items:
        line = format_invoice_line(name, qty, price)
        print(f"  {line}")
        total_invoice += qty * price
    
    print("-" * 40)
    print(f"  ИТОГО К ОПЛАТЕ: {total_invoice:,.2f} руб.")

# ========== ЗАДАНИЕ 9 ==========
def test_task9():
    """Тестирование пары функций get_revenues + analyze."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 9: Ввод и анализ выручки")
    print("=" * 60)
    
    # НОВОЕ количество месяцев: 5 (было 4)
    n = 5
    
    # Получаем данные от пользователя
    revenues = get_revenues(n)
    
    # Анализируем
    mn, mx, avg = analyze(revenues)
    
    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА:")
    print("-" * 40)
    print(f"Минимальная выручка:  {mn:12,.2f} руб.")
    print(f"Максимальная выручка: {mx:12,.2f} руб.")
    print(f"Средняя выручка:      {avg:12,.2f} руб.")
    print(f"Размах (max - min):   {mx - mn:12,.2f} руб.")

# ========== ЗАДАНИЕ 10 ==========
def generate_report(company_name, revenue, costs):
    """
    Генерирует и выводит полный финансовый отчёт.
    
    ПАРАМЕТРЫ:
        company_name (str): название компании
        revenue (float): выручка
        costs (float): затраты
    
    ВОЗВРАЩАЕТ:
        None (ничего не возвращает, только выводит на экран)
    """
    profit = revenue - costs
    
    print("\n" + " " * 50)
    print(f" ФИНАНСОВЫЙ ОТЧЁТ: {company_name}")
    print(" " * 50)
    print(f"Выручка:      {revenue:15,.2f} руб.")
    print(f"Затраты:      {costs:15,.2f} руб.")
    print(f"Прибыль:      {profit:15,.2f} руб.")
    
    # Расчёт рентабельности (только если выручка > 0)
    if revenue > 0:
        margin = (profit / revenue) * 100
        print(f"Рентабельность: {margin:14.2f} %")
    else:
        print("Рентабельность: не определена (выручка = 0)")
    
    # Вердикт
    print("─" * 50)
    if profit > 0:
        print(" ВЕРДИКТ: Компания ПРИБЫЛЬНА (рекомендуется масштабирование)")
    elif profit < 0:
        print(" ВЕРДИКТ: Компания УБЫТОЧНА (требуется оптимизация)")
    else:
        print(" ВЕРДИКТ: Компания БЕЗУБЫТОЧНА (нужен рост)")
    print(" " * 50)

def test_task10():
    """Тестирование generate_report с новыми компаниями и числами."""
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 10: Генерация финансовых отчётов")
    print("=" * 60)
    
    # НОВЫЕ компании и НОВЫЕ числа
    companies = [
        ("ООО 'ТехноПрогресс'", 3_800_000, 2_100_000),   # прибыль 1.7 млн
        ("ИП 'Старт'", 620_000, 890_000),                # убыток -270 тыс.
        ("ЗАО 'Гарант'", 1_500_000, 1_500_000)           # ноль
    ]
    
    for name, rev, cost in companies:
        generate_report(name, rev, cost)
