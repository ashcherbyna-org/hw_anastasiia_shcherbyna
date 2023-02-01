

def my_execute():
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