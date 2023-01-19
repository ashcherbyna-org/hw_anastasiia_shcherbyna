# Cashier in the cinema

def is_valid(age):
    """
    :param age: for validation age
    :return: True if is valid. False if not
    """

    if not age.isnumeric():
        print('Введіть число')
        return False
    elif int(age) > 100:
        print('Введіть вірний вік?')
        return False
    return True

def my_execute():
    """

    :return: None
    """
    stop = None
    while not stop:
        age = input('Введіть вік: ')

        conditions(age)
        stop = input("введіть Yes/No щоб продовжити")
        if stop == "No":
            break
        elif stop == "Yes":
            continue
        else:
            print("Некореекктний ввод, виходимо з програми")
            break





def is_similar_number(age_number):
    """

    :param age_number: User age
    :return: True if age have simular number, False if not
    """
    if (age_number % 11) == 0:
        return True
    return False


def add_endings(age):
    """

    :param age: User age
    :return: Correct age pronounce
    """
    last_number = int(age[-1])
    if 11 <= int(age) <= 19:
        return f"{age} pокiв"
    elif 2 <= last_number <= 4:
        return f"{age} pоки"
    elif last_number == 1:
        return f"{age} piк"
    else:
        return f"{age} pокiв"


def conditions(age):
    """

    :param age: User age
    :return: None
    """
    if not is_valid(age):
        return
    age_number = int(age)
    if age_number < 7:
        print(f'Тобі ж {add_endings(age)}! Де твої батьки')
    elif age_number < 16:
        print(f'Тобі лише {add_endings(age)}, а це е фільм для дорослих')
    elif age_number >= 65:
        print(f'Вам {add_endings(age)}? Покажіть пенсійне посвідчення!')
    elif is_similar_number(age_number):
        print(f'О, вам {add_endings(age)}! Який цікавий вік!')

    else:
        print(f'Незважаючи на те, що вам {add_endings(age)}, білетів всеодно нема!')

my_execute()



