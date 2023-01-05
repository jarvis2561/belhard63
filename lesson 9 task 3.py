with open('les9 task 3','r',encoding='utf-8') as file:
    a = file.read()
    lines = 0
    letter = 0
    words = 0
    word = ""
    for a in file:
        if a == '\n':
            lines += 1
        if a.isalpha():
            letters += 1
            word += a
        elif word != "":
            word = ""
            words += 1
print(f'Всего слов:{len(word)}\n,Всего букв: {(letter)}\n,Всего строк:{(lines)} ')
