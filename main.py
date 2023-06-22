


dict_hello = {
    "ua": ["Здоровенькі були", "Привіт", "Доброго дня", "Привітання", "Вітаю"],
    "ru": ["Привет, ребята", "Здравствуйте", "Приветствую", "Приветики", "Здорово"],
    "eng": ["Hello there!", "Hi", "Greetings", "Hey", "Howdy"],
    "it": ["Ciao tutti!", "Salve", "Buongiorno", "Ciao a tutti", "Saluti"]
}

EXIT = 0

option = abs(int(input("Choose your option -> \npress 1 for add localization, \npress 2 for edit localization or translation, \npress 3 for delete localization,\npress 4 for delete translation in localizatios\n->  \npress 0 for exit\n-> ")))
while option != EXIT:

    if option == 1:
        add_lang = input("Do you want to add localization?\nEnter TRUE or FALSE -> ")
        add_lang = add_lang.lower()

        while add_lang == "true":
            new_lang = input("Enter localization -> ")
            translate_to_new_lang = input("Enter translation to your localization -> ")
            dict_hello[new_lang] = [translate_to_new_lang]
            add_lang = input("Do you want to add more localizations? Enter TRUE or FALSE: ").lower()

    if option == 2:
        edit_lang = input("Do you want to edit localization?\nEnter TRUE or FALSE -> ")
        edit_lang = edit_lang.lower()

        while edit_lang == "true":
            lang_to_edit = input("Enter localization to edit -> ")
            val_to_edit = input("Enter translation to your localization -> ")
            dict_hello[lang_to_edit] = [val_to_edit]
            edit_lang = input("Do you want to edit_lang more localizations? Enter TRUE or FALSE: ").lower()
    if option == 3:
        option_del = input("Localization for deletion -> ")
        option_del = option_del.lower()
        del dict_hello[option_del]
    if option == 4:
        option_del = abs(int(input("Do you want to delete all the translations in each localization or leave just 1 translation? For DELETE ALL - press 1, for DELETE translations with 1 value - press 2 -> ")))
        if option_del == 1:
            for i in dict_hello:
                if len(dict_hello[i]) > 1:
                    dict_hello[i] = [dict_hello[i][0]]
        elif option_del == 2:
            for i in dict_hello:
                if len(dict_hello[i]) > 1:
                    dict_hello[i] = []
        else:
            print("Incorrect choice in deletion ! ")
    if option == 0:
        break
    option = abs(int(input("Choose your option -> \npress 1 for add localization, \npress 2 for edit localization or translation, \npress 3 for delete localization,\npress 4 for delete translation in localizatios\n->  \npress 0 for exit\n-> ")))

for i in dict_hello:
    print(i, ":", dict_hello[i])





