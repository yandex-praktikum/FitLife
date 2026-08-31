# -*- coding: utf-8 -*-
import sys
import io

# Перенаправляем stdout и stderr в UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
# Все что выше, написано благодаря ИИ,
# так как из-за проблем с кодировкой я не мог пройти тесты,
# возвращалась ошибка UnicodeDecodeError


# Проект FitLife - MVP версия 1.0
DAILY_WATER_ML = 30

print('''Приветствую Вас в FitLife!
Предлагаю Вам заполнить небольшую анкету.''')
print('Как я могу к Вам обращаться?', end=' ')
user_name = input().title()
print('Напишите Ваш возраст:', end=' ')
user_age = int(input())
print('Напишите Ваш вес (в кг):', end=' ')
user_weight = float(input())
print('Напишите Ваш рост (в см):', end=' ')
user_height = float(input())
print('Приступаю к расчетам!')

# Считаем Индекс Массы Тела
bmi = round(user_weight / (user_height ** 2), 1)
# Считаем дневную норму воды
water_needed_l = round((user_weight * DAILY_WATER_ML) / 1000, 3)

print("=" * 40)
print(f'''Отчет для пользователя: {user_name} ({user_age} г.)
Ваш Индекс Массы Тела: {bmi}
Рекомендуемая норма воды: {water_needed_l} л. в день
Будьте здоровы и всего Вам хорошего!''')
print("=" * 40)
