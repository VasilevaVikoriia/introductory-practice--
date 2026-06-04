"""
Модуль 2. Условия и циклы.



    """1. Результат периода (прибыль/убыток/ноль) - порог: 5000 руб."""
    print("\n--- Задание 1: Результат периода ---")
    profit = float(input("Введите прибыль за месяц (руб): "))
    if profit > 5000:
        print(" Прибыль (выше 5000 руб.)")
    elif profit < 0:
        print(" Убыток")
    else:
        print(" Безубыточность (0–5000 руб.)")

    """2. Категория бизнеса: новые границы (2, 15, 200 млн руб)."""
    print("\n--- Задание 2: Категория бизнеса ---")
    revenue = float(input("Введите годовую выручку (млн руб): ")) * 1_000_000
    if revenue < 2_000_000:
        print(" Микробизнес (до 2 млн)")
    elif revenue < 15_000_000:
        print(" Малый бизнес (2–15 млн)")
    elif revenue < 200_000_000:
        print(" Средний бизнес (15–200 млн)")
    else:
        print(" Крупный бизнес (выше 200 млн)")


    """3. НДФЛ: прогрессивная шкала (12% до 40 000, 18% до 120 000, 22% выше)."""
    print("\n--- Задание 3: Расчёт НДФЛ (прогрессивная шкала) ---")
    salary = float(input("Введите зарплату (руб): "))
    if salary <= 40000:
        tax_rate = 0.12
    elif salary <= 120000:
        tax_rate = 0.18
    else:
        tax_rate = 0.22
    tax = salary * tax_rate
    on_hands = salary - tax
    print(f"Ставка: {tax_rate*100:.0f}%")
    print(f"Налог: {tax:.2f} руб.")
    print(f"На руки: {on_hands:.2f} руб.")


    """4. Таблица умножения: пользователь вводит ставку, умножаем на 3,6,9,12."""
    print("\n--- Задание 4: Таблица умножения ставки (шаг 3) ---")
    rate = float(input("Введите процентную ставку (%): "))
    print(f"Таблица умножения для {rate}% (×3, ×6, ×9, ×12):")
    for i in range(3, 13, 3):
        print(f"{rate} × {i} = {rate * i:.2f}")


    """5. Анализ цен: пользователь вводит 5 цен и порог."""
    print("\n--- Задание 5: Анализ цен ---")
    prices = []
    for i in range(1, 6):
        price = float(input(f"Введите цену товара {i}: "))
        prices.append(price)
    threshold = float(input("Введите порог 'ДОРОГО' (руб): "))
    print("\nРезультаты:")
    for idx, price in enumerate(prices, 1):
        if price > threshold:
            print(f"Товар {idx}: {price} руб. —  ДОРОГО")
        elif price < threshold * 0.5:
            print(f"Товар {idx}: {price} руб. —  ДЕШЁВО")
        else:
            print(f"Товар {idx}: {price} руб. —  СРЕДНЯЯ ЦЕНА")


    """6. Рост вклада: пользователь вводит капитал, ставку и количество лет."""
    print("\n--- Задание 6: Рост вклада (сложный процент) ---")
    capital = float(input("Введите начальный капитал (руб): "))
    rate = float(input("Введите годовую ставку (%): ")) / 100
    years = int(input("На сколько лет (лет): "))
    print(f"\nСтарт: {capital:.2f} руб., ставка {rate*100}%")
    for year in range(1, years + 1):
        capital *= (1 + rate)
        print(f"Год {year}: {capital:,.2f} руб.")


    """7. Накопительный счёт: пользователь вводит взнос, месяцы, бонус каждые 3 месяца."""
    print("\n--- Задание 7: Накопительный счёт ---")
    monthly = float(input("Ежемесячный взнос (руб): "))
    months = int(input("Количество месяцев: "))
    bonus_rate = float(input("Бонусная ставка каждые 3 месяца (%): ")) / 100
    total = 0
    for m in range(1, months + 1):
        total += monthly
        if m % 3 == 0:
            bonus = total * bonus_rate
            total += bonus
            print(f"Месяц {m}: {total:.2f} руб. (+ бонус {bonus:.2f})")
        else:
            print(f"Месяц {m}: {total:.2f} руб.")

    """8. Доступность: пользователь вводит бюджет и 5 цен товаров."""
    print("\n--- Задание 8: Доступность товаров ---")
    budget = float(input("Ваш бюджет (руб): "))
    prices = []
    for i in range(1, 6):
        price = float(input(f"Цена товара {i}: "))
        prices.append(price)


t("\nРезультаты:")
    for i, price in enumerate(prices, 1):
        if price <= budget:
            print(f"Товар {i} ({price} руб.) —  доступен")
        else:
            need = price - budget
            print(f"Товар {i} ({price} руб.) —  не хватает {need} руб.")


    """9. Выручка за полгода: пользователь вводит 6 значений."""
    print("\n--- Задание 9: Анализ выручки за 6 месяцев ---")
    revenues = []
    for m in range(1, 7):
        rev = float(input(f"Выручка за месяц {m} (руб): "))
        revenues.append(rev)
    print(f"\n Минимум: {min(revenues):.2f} руб.")
    print(f" Максимум: {max(revenues):.2f} руб.")
    print(f" Среднее: {sum(revenues)/len(revenues):.2f} руб.")
    print(f" Размах: {max(revenues) - min(revenues):.2f} руб.")


    """10. Рентабельность: пользователь вводит порог и 6 значений."""
    print("\n--- Задание 10: Анализ рентабельности ---")
    threshold = float(input("Введите пороговую рентабельность (%): "))
    values = []
    for m in range(1, 7):
        val = float(input(f"Рентабельность месяца {m} (%): "))
        values.append(val)
    months_above = 0
    print(f"\nПорог: {threshold}%")
    for idx, val in enumerate(values, 1):
        if val > threshold:
            months_above += 1
            print(f"Месяц {idx}: {val}% —  выше порога")
        else:
            print(f"Месяц {idx}: {val}% —  ниже или равно")
    print(f"\n Итог: {months_above} из 6 месяцев выше порога ({months_above/6*100:.0f}%)")


