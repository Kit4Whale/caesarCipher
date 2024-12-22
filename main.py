def ru_encoder(text, key):
    res = ""
    for i in range(len(text)):
        if text[i].isalpha():
            res += chr(ord(text[i]) + key)
        else:
            res += text[i]
    print(res)

def en_encoder(text, key):
    pass

def ru_decoder(text):
    pass

def en_decoder(text):
    pass




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


