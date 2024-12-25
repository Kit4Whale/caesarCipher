def ru_encoder(text, key):
    for i in range(len(text)):
        if text[i] in ru_up_al:
            print(ru_up_al[(ru_up_al.index(text[i]) + key) % len(ru_up_al)], end="")
        elif text[i] in ru_lo_al:
            print(ru_lo_al[(ru_lo_al.index(text[i]) + key) % len(ru_lo_al)], end="")
        else:
            print(text[i], end="")

def en_encoder(text, key):
    for i in range(len(text)):
        if text[i] in en_up_al:
            print(en_up_al[(en_up_al.index(text[i]) + key) % len(en_up_al)], end="")
        elif text[i] in en_lo_al:
            print(en_lo_al[(en_lo_al.index(text[i]) + key) % len(en_lo_al)], end="")
        else:
            print(text[i], end="")

def ru_decoder(text, key):
    for i in range(len(text)):
        if text[i] in ru_up_al:
            print(ru_up_al[(ru_up_al.index(text[i]) - key) % len(ru_up_al)], end="")
        elif text[i] in ru_lo_al:
            print(ru_lo_al[(ru_lo_al.index(text[i]) - key) % len(ru_lo_al)], end="")
        else:
            print(text[i], end="")

def en_decoder(text):
    for i in range(len(text)):
        if text[i] in en_up_al:
            print(en_up_al[(en_up_al.index(text[i]) - key) % len(en_up_al)], end="")
        elif text[i] in en_lo_al:
            print(en_lo_al[(en_lo_al.index(text[i]) - key) % len(en_lo_al)], end="")
        else:
            print(text[i], end="")


en_lo_al = 'abcdefghijklmnopqrstuvwxyz'
en_up_al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lo_al = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_up_al = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print("Добро пожаловать в Шифратор/Дешифратор Цезаря!")

print("шифрование или дешифрование? (e/d): ", end="")
type = input()

print("русский или английский? (ru/en): ", end="")
language = input()

print("шаг сдвига (число): ", end="")
key = int(input())

print("Введите текст: ", end="")
text = input()

if type == "e":
    if language == "ru":
        ru_encoder(text, key)
    if language == "en":
        en_encoder(text, key)

if type == "d":
    if language == "ru":
        ru_decoder(text, key)
    if language == "en":
        en_decoder(text, key)


