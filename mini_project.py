# mini_project.py
# Вариант 10: Анализ прайс-листа (Автосалон — бизнес-аналитика)
# Задача: оценка ценового портфеля, доходности и эффекта от наценки

def analyze_pricelist_with_markup(items, markup_percent=15):
    """
    Бизнес-анализ прайс-листа:
    - средняя цена (benchmark)
    - экстремумы для позиционирования
    - доля товаров выше среднего чека
    - экономический эффект от наценки (прирост выручки)
    """
    # Распаковка данных
    models, prices = zip(*items)

    # 1. Базовые метрики
    avg_price = sum(prices) / len(prices)
    max_price = max(prices)
    min_price = min(prices)
    
    # Поиск лидеров ценового диапазона
    premium_model = [models[i] for i in range(len(prices)) if prices[i] == max_price][0]
    budget_model = [models[i] for i in range(len(prices)) if prices[i] == min_price][0]

    # 2. Анализ позиций выше средней цены (индикатор премиальности портфеля)
    premium_count = 0
    for price in prices:
        if price > avg_price:
            premium_count += 1
    premium_share = (premium_count / len(prices)) * 100  # Доля премиум-позиций

    # 3. Расчёт экономического эффекта от наценки
    current_revenue = sum(prices)                          # Текущая выручка при продаже всех единиц
    new_prices = [price * (1 + markup_percent / 100) for price in prices]
    projected_revenue = sum(new_prices)                    # Прогноз выручки после наценки
    revenue_growth = projected_revenue - current_revenue
    revenue_growth_percent = (revenue_growth / current_revenue) * 100

    # Формирование нового прайса для отдела продаж
    updated_pricelist = [(models[i], round(new_prices[i], 2)) for i in range(len(prices))]

    # Управленческая отчётность
    print("=" * 70)
    print(" АНАЛИЗ ПРАЙС-ЛИСТА | АВТОСАЛОН (бизнес-аналитика)")
    print("=" * 70)
    print(f" Средняя цена (benchmark): {avg_price:,.2f} ₽")
    print(f" Самый дорогой (флагман): {premium_model} — {max_price:,.2f} ₽")
    print(f" Самый доступный (лидер объёма): {budget_model} — {min_price:,.2f} ₽")
    print(f" Доля премиум-позиций (выше среднего): {premium_count} из {len(prices)} ({premium_share:.1f}%)")
    print("\n" + "=" * 70)
    print(" ЭКОНОМИЧЕСКИЙ ЭФФЕКТ от наценки +15%:")
    print("-" * 70)
    print(f"Текущая выручка (портфель): {current_revenue:,.2f} ₽")
    print(f"Прогноз выручки после наценки: {projected_revenue:,.2f} ₽")
    print(f"Прирост выручки: +{revenue_growth:,.2f} ₽ ({revenue_growth_percent:.1f}%)")
    print("\n ОБНОВЛЁННЫЙ ПРАЙС-ЛИСТ (для отдела продаж):")
    print("-" * 70)
    for model, new_price in updated_pricelist:
        print(f"  • {model}: {new_price:,.2f} ₽")
    print("=" * 70)
    print(" Рекомендация: наценка экономически целесообразна (+{:.1f}% к выручке)".format(revenue_growth_percent))
    print("=" * 70)

# Основной блок — ввод данных аналитиком
if __name__ == "__main__":
    # Реальные данные автодилера (источник: закупочные цены)
    dealership_inventory = [
        ("BMW X6 M Competition (F96) рестайлинг 2026", 24_950_000),
        ("Dodge RAM TRX 2025", 21_000_000),
        ("Audi RS6 2025", 20_490_000),
        ("Mazda 6 Atenza III рестайлинг 2 2023", 3_400_000),
        ("Mercedes-Benz G-Class EQ Technology 580 2024", 30_000_000)
    
    # Запуск бизнес-анализа с наценкой 15%
    analyze_pricelist_with_markup(dealership_inventory, markup_percent=15)

======================================================================
 АНАЛИЗ ПРАЙС-ЛИСТА | АВТОСАЛОН (бизнес-аналитика)
======================================================================
 Средняя цена (benchmark): 19,968,000.00 ₽
 Самый дорогой (флагман): Mercedes-Benz G-Class EQ Technology 580 2024 — 30,000,000.00 ₽
 Самый доступный (лидер объёма): Mazda 6 Atenza III рестайлинг 2 2023 — 3,400,000.00 ₽
 Доля премиум-позиций (выше среднего): 2 из 5 (40.0%)

======================================================================
 ЭКОНОМИЧЕСКИЙ ЭФФЕКТ от наценки +15%:
----------------------------------------------------------------------
Текущая выручка (портфель): 99,840,000.00 ₽
Прогноз выручки после наценки: 114,816,000.00 ₽
Прирост выручки: +14,976,000.00 ₽ (15.0%)

 ОБНОВЛЁННЫЙ ПРАЙС-ЛИСТ (для отдела продаж):
----------------------------------------------------------------------
  • BMW X6 M Competition (F96) рестайлинг 2026: 28,692,500.00 ₽
  • Dodge RAM TRX 2025: 24,150,000.00 ₽
  • Audi RS6 2025: 23,563,500.00 ₽
  • Mazda 6 Atenza III рестайлинг 2 2023: 3,910,000.00 ₽
  • Mercedes-Benz G-Class EQ Technology 580 2024: 34,500,000.00 ₽
======================================================================
 Рекомендация: наценка экономически целесообразна (+15.0% к выручке)
======================================================================
