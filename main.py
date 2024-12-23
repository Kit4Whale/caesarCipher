def ru_encoder(text, key):
    res = ""
    for i in range(len(text)):
        if text[i] in ru_up_al:
            print(ru_up_al[(ru_up_al.index(text[i]) + key) % len(ru_up_al)], end="")
        if text[i] in ru_lo_al:
            print(ru_lo_al[(ru_lo_al.index(text[i]) + key) % len(ru_lo_al)], end="")
        if text[i] in en_up_al:
            print(en_up_al[(en_up_al.index(text[i]) + key) % len(en_up_al)], end="")
        if text[i] in en_lo_al:
            print(en_lo_al[(en_lo_al.index(text[i]) + key) % len(en_lo_al)], end="")
        else:
            print(text[i], end="")
    print(res)

def en_encoder(text, key):
    pass

def ru_decoder(text):
    pass

def en_decoder(text):
    pass


en_lo_al = 'abcdefghijklmnopqrstuvwxyz'
en_up_al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lo_al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_up_al = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print("Добро пожаловать в Шифратор/Дешифратор Цезаря!")

print("шифрование или дешифрование? (En/De): ", end="")
type = input()

print("русский или английский? (Ru/En): ", end="")
language = input()

print("шаг сдвига (число): ", end="")
key = int(input())

print("Введите текст: ", end="")
text = input()

if type == "En":
    if language == "Ru":
        ru_encoder(text, key)
    if language == "En":
        en_encoder(text, key)

if type == "De":
    if language == "Ru":
        ru_decoder(text)
    if language == "En":
        en_decoder(text)


