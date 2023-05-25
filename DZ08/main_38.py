# Задача 38: Дополнить телефонный справочник с возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

phonebook = {}

def insert(name, phone):
    phonebook[name] = phone

def update(name, phone):
    if name in phonebook:
        phonebook[name] = phone
    else:
        return(f'Запись с именем {name} не найдена.')

def delete(name):
    if name in phonebook:
        del phonebook[name]
    else:
        return(f'Запись с именем {name} не найдена.')

def select(name):
    if name in phonebook:
        return (f'{phonebook[name]} - {name}')
    else:
        return(f'Номер {name} не найден.')


insert('Иван', '8 800 700-68-40')
insert('Мария', '8 800 700-68-42')
print('------------------------ Добавление номера')
print(select('Иван'))
print(select('Мария'))
print('------------------------ Изменение нмера')
update('Иван', '8 800 700-68-41')
print(select('Иван'))
print('------------------------ Поиск номера')
delete('Мария')
print(select('Мария'))
print('------------------------')