
alphabet = (
    "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й",
    "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
    "х", "ц", "ч", "ш", "щ", "ь", "ы", "ъ", "э", "ю", "я",
)

print('Вас приветствует игра "хреновый программист"')

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Укажи свой пол (м/ж)\n'),
         'pet_name': input('Как зовут твоего питомца?\n'),
         'likes_playing': bool(input("Любишь играть? (да/нет) \n"))
         }

if gamer['age'] > 18:
    if gamer['age'] <= 90:
        print("Привет ", gamer['name'])
    else:
        answer = input('Для вас это может быть утомительно, уверены что хотите играть? \n')
        if str(answer) == 'да':
            answer = input('Точно уверены?\n')
            if str(answer) == 'да':
                print("Хорошо, тогда начнём игру")
            elif answer == 'нет':
                print("Тогда до свидания ", gamer['name'])
                exit()
            else:
                print('Вы даже ответ вписать нормально не в состоянии, до свидания')
                exit()
        elif answer == 'нет':
            print("Тогда до свидания ", gamer['name'])
            exit()
        else:
            print('Вы даже ответ вписать нормально не в состоянии, до свидания')
            exit()
else:
    print("тебе играть нельзя")
    exit()

print('Я могу назвать буквы алфавита, которых нет в твоем имени:')

for char in alphabet:
    if char not in gamer['name']:
        print(char)
