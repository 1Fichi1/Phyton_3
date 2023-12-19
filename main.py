import random
import datetime
import time
import json
import os
import csv

username = input("Введите имя пользователя: ")


def delete_save():
    save_name = input("Введите название сохранения для удаления: ")
    try:
        os.remove(f"{save_name}.json")
        print(f"Сохранение '{save_name}' удалено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def load_save(save_name):
    try:
        with open(f"{save_name}.json", "r") as file:
            game_data = json.load(file)
            print(f"Сохранение '{save_name}' успешно загружено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def read_data_from_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def write_data_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


inventory = set()
room_descriptions = {
    'entrance': 'Вы находитесь у входа в мистический лес. Перед вами два пути: вглубь леса и наружу.',
    'deep_forest': 'Вы находитесь в глубине мистического леса. Вокруг вас шумят деревья и слышны странные звуки.',
    'outside': 'Вы вернулись обратно к входу в лес. Что вы будете делать?',
    'clearing': 'Вы попали на лесную поляну, где растут диковинные растения.',
    'river_bank': 'Вы находитесь у берега реки. Переплыть или вернуться назад?',
    'cave_entrance': 'Перед вами вход в темную пещеру. Внутри может быть что-то интересное.',
    'inside_cave': 'Вы внутри пещеры. Тут темно и мрачно.',
    'artifact_room': 'Вы нашли комнату с утерянным артефактом. Поздравляем!'
}

characters = {
    'elf': {
        'name': 'Эльф',
        'dialog': 'Здравствуй, странник. Ты ищешь утерянный артефакт?'
    },
    'troll': {
        'name': 'Тролль',
        'dialog': 'Стой, кто идет? Проходить мимо меня нельзя без моего разрешения.'
    },
    'spirit': {
        'name': 'Дух Леса',
        'dialog': 'Ты чувствуешь энергию этого места?'
    }
}


def describe_room(room):
    print(room_descriptions[room])


def add_to_inventory(item):
    inventory.add(item)
    print(f'Вы добавили "{item}" в инвентарь.')


def interact_with_room(room):
    if room == 'artifact_room':
        add_to_inventory('магический артефакт')


def interact_with_character(character):
    if character == 'elf':
        print(f'{characters[character]["name"]}: {characters[character]["dialog"]}')
        response = input('1. Да, и я прошу помощи'
                         '\n2. Нет, я сам найду'
                         '\nВаш выбор: ')
        if response == '1':
            print(f'{characters[character]["name"]}: Тогда следуй за мной.')
        elif response == '2':
            print(f'{characters[character]["name"]}: Пусть удача сопутствует тебе.')
    elif character == 'troll':
        print(f'{characters[character]["name"]}: {characters[character]["dialog"]}')
        print('1. Попробовать уговорить тролля\n2. Вернуться обратно')
        choice = input('Ваш выбор: ')
        if choice == '1':
            print(f'{characters[character]["name"]}: Хорошо, ты можешь пройти.')
        else:
            print(f'{characters[character]["name"]}: Никто не пройдет без разрешения.')
    elif character == 'spirit':
        print(f'{characters[character]["name"]}: {characters[character]["dialog"]}')
        print('1. Поговорить с духом\n2. Продолжить свой путь')
        choice = input('Ваш выбор: ')
        if choice == '1':
            print(f'{characters[character]["name"]}: Ты обладаешь мудростью, чтобы пройти дальше.')
        else:
            print(f'{characters[character]["name"]}: Ты свободен идти куда хочешь.')


def play_game():
    current_room = 'entrance'
    while True:
        describe_room(current_room)
        if current_room == 'entrance':
            action = input('1. Пойти вглубь леса'
                           '\n2. Покинуть лес'
                           '\nВыберите действие: ')
            if action == '1':
                current_room = 'deep_forest'
            elif action == '2':
                poka = 'Вы покинули мистический лес. Игра завершена.'
                for char in poka:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
            else:
                ladno = 'Неверный выбор. Попробуйте еще раз.'
                for char in ladno:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
        elif current_room == 'deep_forest':
            action = input('1. Исследовать лес'
                           '\n2. Пойти к реке'
                           '\n3. Вернуться к входу'
                           '\nВыберите действие: ')
            if action == '1':
                current_room = 'clearing'
            elif action == '2':
                current_room = 'river_bank'
            elif action == '3':
                current_room = 'entrance'
            else:
                ladno = 'Неверный выбор. Попробуйте еще раз.'
                for char in ladno:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
        elif current_room == 'clearing':
            action = input('1. Подойти к цветущим растениям'
                           '\n2. Вернуться в лес'
                           '\nВыберите действие: ')
            if action == '1':
                interact_with_character('elf')
                current_room = 'artifact_room'
            elif action == '2':
                current_room = 'deep_forest'
            else:
                ladno = 'Неверный выбор. Попробуйте еще раз.'
                for char in ladno:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
        elif current_room == 'river_bank':
            action = input('1. Попробовать переплыть реку'
                           '\n2. Вернуться в лес'
                           '\nВыберите действие: ')
            if action == '1':
                current_room = 'cave_entrance'
            elif action == '2':
                current_room = 'deep_forest'
            else:
                ladno = 'Неверный выбор. Попробуйте еще раз.'
                for char in ladno:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
        elif current_room == 'cave_entrance':
            action = input('1. Войти в пещеру'
                           '\n2. Вернуться к реке'
                           '\nВыберите действие: ')
            if action == '1':
                current_room = 'inside_cave'
            elif action == '2':
                current_room = 'river_bank'
            else:
                ladno = 'Неверный выбор. Попробуйте еще раз.'
                for char in ladno:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
        elif current_room == 'inside_cave':
            action = input('1. Исследовать пещеру'
                           '\n2. Выйти из пещеры'
                           '\nВыберите действие: ')
            if action == '1':
                current_room = 'artifact_room'
            elif action == '2':
                current_room = 'cave_entrance'
            else:
                ladno = 'Неверный выбор. Попробуйте еще раз.'
                for char in ladno:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
        elif current_room == 'artifact_room':
            print('Поздравляем! Вы нашли утерянный магический артефакт. Игра завершена.')
            print('1-сохранение' )
            choice = input("\nВыберите действие 1: ")
            if choice == "1":
                data = read_data_from_csv("data.csv")
                if username != "":
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data.append([username, current_time])
                    write_data_to_csv("data.csv", data)
                save_name = input("Введите название сохранения: ")
                game_data = {
                    "Концовка": "Молодец, что прошел мою игру."
                }
                with open(f"{save_name}.json", "w") as file:
                    json.dump(game_data, file)
            break


if __name__ == '__main__':
    Gameus = 'Добро пожаловать в игру "Поиск утерянного артефакта в мистическом лесу"!'
    for char in Gameus:
        print(char, end='', flush=True)
        time.sleep(0.1)
    play_game()