import argparse
import logging
from random import randint

logging.basicConfig(filename='log_game.log', level=logging.INFO, encoding='utf-8')

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def go_game():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    for i in range(1,11):
        try:
            value = input(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}: ")
            user_num = int(value)
            if user_num == num:
                print("Поздравляю!!!")
                logging.info(f"Пользователь угадал число с {i} попытки")
                break
            elif user_num < num:
                print("Больше")
                logging.info(f"Загаданное число больше введенного пользователем числа.Попытка № {i}")
            else:
                print("Меньше")
                logging.info(f"Загаданное число меньше введенного пользователем числа.Попытка № {i}")
        except ValueError:
            print(f"Ошибка! Введите целое число от {LOWER_LIMIT} до {UPPER_LIMIT}.")
            logging.error("Пользователь ввел некорректное значение")
    else:
        print(f"Вы не угадали число. Было загадано число {num}.")
        logging.info(f"Пользователь не угадал число. Было загадано число {num}.")


parser = argparse.ArgumentParser(description='Game')
parser.add_argument('--lower', type=int, help='Нижний предел для игры')
parser.add_argument('--upper', type=int, help='Верхний предел для игры')
args = parser.parse_args()

if args.lower:
    LOWER_LIMIT = args.lower
if args.upper:
    UPPER_LIMIT = args.upper


go_game()
# Например: python task1.py --lower 0 --upper 99