"""
Twoim zadaniem jest:

Napisać funkcję add_person(name, age),
która dodaje nową osobę do bazy danych.

*Napisać funkcję get_age(name),
która zwraca wiek osoby o podanym imieniu.

*Napisać funkcję update_age(name, new_age),
która aktualizuje wiek osoby o podanym imieniu.

*Napisać funkcję delete_person(name),
która usuwa osobę o podanym imieniu z bazy danych
"""

def add_person(name, age):
    with open("database.txt", "a") as file:
        file.write(f'{name}, {age}\n')

def get_age(name):
    with open("database.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            person_name, person_age = line.strip().split(",")
            if person_name == name:
                return person_age
    return "brak danych"

# add_person("Tomek", 45)
print(get_age("Krzysztof"))