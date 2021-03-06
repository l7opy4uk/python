
## Недоделаный словарь.
def vocabulary():
    choice = None
    swords = {"Фальшион": "Европейское клинковое оружие с расширяющимся к концу коротким клинком с односторонней заточкой.",
                      "Шпага": "Холодное колюще-рубящее или колющее оружие, производное от меча, состоящее из длинного (около 1 метра и более), прямого одно-двухлезвийного или гранёного клинка и рукояти (эфеса) с дужкой и гардой различной формы. ",
                      "Рапира": "Преимущественно колющее клинковое оружие, разновидность шпаги, в изначальном значении длинная «гражданская» шпага, в отличие от «боевой» шпаги слишком лёгкая для нанесения рубящего удара, тем не менее в классическом (не спортивном) варианте имеющая лезвия.",
                      "Сабля": "Рубяще-режущее и колюще-режущее клинковое холодное оружие. Клинок сабли, как правило, однолезвийный (в ряде случаев — с полуторной заточкой), имеет характерный изгиб в сторону обуха. ",
                      "Катана": "Рубяще-режущее и колюще-режущее клинковое холодное оружие. Клинок сабли, как правило, однолезвийный (в ряде случаев — с полуторной заточкой), имеет характерный изгиб в сторону обуха. "}
    while choice != "0":
        print(
        """
        Различные виды клинкового оружия:
        0 - Выйти
        1 - Найти толкование тервина
        2 - Добавить термин
        3 - Изменить толкование
        4 - Удалить термин
        5 - Вывести список доступных терминов
        """
        )
        choice = input("Ваш выбор: ")
        if choice == "0":
            print("До свидания.")
        elif choice == "1":
            outputWord = input("Введите слово: ")
            print(swords.get(outputWord.capitalize(), "Отсутствует в словаре"))
            input("Нажмите Enter для выхода в \"Меню\"")
        elif choice == "2":
            termInput = input("Какой вид клинкового оружия вы хотите добавить? ")
            term = termInput.capitalize()
            if term.capitalize() not in swords:
                definition = input("Введите описание клинка: ")
                swords[term] = definition.capitalize()
                print("\nТермин", term, "добавлен в список")
            else:
                print("\nТакой тип уже есть, попробуйте изменить его толкование!")
        elif choice == "3":
            termInput = input("Какой термин вы хотите переопределить? ")
            term = termInput.capitalize()
            if term in swords:
                definition = input("Введите термин: ")
                swords[term] = definition
                print("\nТермин", term, "переопределен")
            else:
                print("Такого термина пока нет! Попробуйте добавить ежго в словарь")
        elif choice == "4":
                termInput = input("Какой термин вы хотите удалить? ")
                term = termInput.capitalize()
                if term in swords:
                    del swords[term]
                    print("\nТермин", term, "удален")
                else:
                    print("\nНичем не могу помочь. Терсина", term, "нет в словаре.")
        elif choice == "5":
            print("\n",swords.keys(term))
        else:
            input("Выбор некорректен, попробуйте еще раз.")



        



    

