def ru_encoder(text, key):
    for i in range(len(text)):
        if text[i] in RU_UP_AL:
            print(RU_UP_AL[(RU_UP_AL.index(text[i]) + key) % len(RU_UP_AL)], end="")
        elif text[i] in RU_LO_AL:
            print(RU_LO_AL[(RU_LO_AL.index(text[i]) + key) % len(RU_LO_AL)], end="")
        else:
            print(text[i], end="")

def en_encoder(text, key):
    for i in range(len(text)):
        if text[i] in EN_UP_AL:
            print(EN_UP_AL[(EN_UP_AL.index(text[i]) + key) % len(EN_UP_AL)], end="")
        elif text[i] in EN_LO_AL:
            print(EN_LO_AL[(EN_LO_AL.index(text[i]) + key) % len(EN_LO_AL)], end="")
        else:
            print(text[i], end="")

def ru_decoder(text, key):
    for i in range(len(text)):
        if text[i] in RU_UP_AL:
            print(RU_UP_AL[(RU_UP_AL.index(text[i]) - key) % len(RU_UP_AL)], end="")
        elif text[i] in RU_LO_AL:
            print(RU_LO_AL[(RU_LO_AL.index(text[i]) - key) % len(RU_LO_AL)], end="")
        else:
            print(text[i], end="")

def ru_decoder_without_shift(text):
    for i in range(1, len(RU_LO_AL) + 1):
        print(i, ": ", sep="", end="")
        ru_decoder(text, i)
        print("")

def en_decoder(text, key):
    for i in range(len(text)):
        if text[i] in EN_UP_AL:
            print(EN_UP_AL[(EN_UP_AL.index(text[i]) - key) % len(EN_UP_AL)], end="")
        elif text[i] in EN_LO_AL:
            print(EN_LO_AL[(EN_LO_AL.index(text[i]) - key) % len(EN_LO_AL)], end="")
        else:
            print(text[i], end="")

def en_decoder_without_shift(text):
    for i in range(1, len(EN_LO_AL) + 1):
        print(i, ": ", sep="", end="")
        en_decoder(text, i)
        print("")

def flager_for_three(answer):
    while True:
        if answer == "1" or answer == "2" or answer == "3":
            return answer
        else:
            print("Введено не валидное значение")
            print("Укажите (1/2/3): ", end="")
            answer = input()

def flager_for_two(answer):
    while True:
        if answer == "1" or answer == "2":
            return answer
        else:
            print("Введено не валидное значение")
            print("Укажите (1/2): ", end="")
            answer = input()


EN_LO_AL = 'abcdefghijklmnopqrstuvwxyz'
EN_UP_AL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RU_LO_AL = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RU_UP_AL = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


print("Добро пожаловать в Шифратор/Дешифратор Цезаря!")

print("1:шифрование, 2:дешифрование, 2:дешифрование 3:дешифрование без сдвига?: ", end="")
type = input()
flager_for_three(type)

print("1:русский или 2:английский?: ", end="")
language = input()
flager_for_two(language)

if type != "3":
    print("шаг сдвига (число): ", end="")
    key = int(input())

print("Введите текст: ", end="")
text = input()


if type == "1":
    if language == "1":
        ru_encoder(text, key)
    if language == "2":
        en_encoder(text, key)

if type == "2":
    if language == "1":
        ru_decoder(text, key)
    if language == "2":
        en_decoder(text, key)

if type == "3":
    if language == "1":
        ru_decoder_without_shift(text)
    if language == "2":
        en_decoder_without_shift(text)