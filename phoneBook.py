# Показать все контакты в справочнике

def show_contact():
    with open('data.txt', 'r+', encoding='utf-8') as file:
        book = file.read()
    return book


# Имя

def input_firstname():
    first = input("\nВведи имя: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


# Фамилия

def input_lastname():
    last = input("\nВведи фамилию: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


# Сохраняем новый контакт

def new_contact():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("\nВведи телефон: ")
    contactDetails = ("["+firstname + " " + lastname +
                      ", " + phoneNum + "]\n")
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(contactDetails)
    print(contactDetails + "\nКонтакт успешно сохранён!")


# Поиск контакта

def search_contact():
    searchname = input("\nВведите имя для поиска: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open('data.txt', 'r+', encoding='utf-8') as file:
        filecontents = file.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("\nРезультат:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("\nНе найдено", searchname)


# Изменение контакта

def change_person():
    searchname = input("\nКакой контакт хотите изменить? ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open('data.txt', 'r', encoding='utf-8') as file:
        file_contents = file.readlines()
        found = False
        for line in file_contents:
            if searchname in line:
                print(end=" ")
                print(line)
                found = True
                break
    with open("data.txt", "w", encoding='utf-8') as file:
        for lines in file_contents:
            if line.strip(" ") != lines:
                file.write(lines)
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("\nВведи телефон: ")
    contactDetails = ("["+firstname + " " + lastname +
                      ", " + phoneNum + "]\n")
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(contactDetails)
    print(contactDetails + "\nКонтакт успешно сохранён!")
    

# Удаление контакта

def delete_contact():
    searchname = input("\nКакое имя хотите удалить? ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    with open('data.txt', 'r', encoding='utf-8') as file:
        file_contents = file.readlines()
        found = False
        for line in file_contents:
            if searchname in line:
                print("\nУдалено:", end=" ")
                print(line)
                found = True
                break
    with open("data.txt", "w", encoding='utf-8') as file:
        for lines in file_contents:
            if line.strip(" ") != lines:
                file.write(lines)


# Меню

def main_menu():
    while True:
        print("\nМеню\n")
        print("1. Показать все контакты")
        print("2. Добавить новый контакт")
        print("3. Поиск контакта")
        print("4. Изменение контакта")
        print("5. Удаление контакта")
        print("6. Выход")
        choice = input("\nВведи нужное: ")
        if choice == "1":
            print(show_contact())
        elif choice == "2":
            print(new_contact())
        elif choice == "3":
            print(search_contact())
        elif choice == "4":
            change_person()
        elif choice == "5":
            delete_contact()    
        elif choice == "6":
            print("\nДо свидания!")
            break


# Запуск

main_menu()
