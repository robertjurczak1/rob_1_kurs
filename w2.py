valid_dict =[
    {"name": "Tomek", "age": "25"},
    {"name": "Ania", "age": "10"},
    {"name": "Zbyszek", "age": "17"},
]

invalid_dict =[
    {},
    {"name": "Ania", "age": "10"},
    {"name": "Zbyszek", "age": "17"},
]

invalid_dict2 =[
    {"name": "Tomek", "age": "ert"},
    {"name": "Ania", "age": "10"},
    {"name": "Zbyszek", "age": "17"},
]

def sprawdz_wiek(users, age):
    count = 0
    for user in users:
        try:
            # if int(user["age"]) < age:
            #     count = 1
            user_age = int(user["age"])
        except KeyError:
            print(f"Niepoprawne dane: {user}")
        except ValueError:
            print(f"Niepoprawny wiek: {user}")
        else:
            count += 1 if user_age < age else 0
        finally:
            print(f"Wydruk słownika: {user}")
    return count

print(sprawdz_wiek(valid_dict,11))
print(sprawdz_wiek(invalid_dict,11))
print(sprawdz_wiek(invalid_dict2,11))

