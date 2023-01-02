with open('file.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    print(a)
a = a.split()

g = 'аеёиоуыэюя'
sg = 'бвгджзйклмнпрстфхчцшщ'
gct, sgct = 0, 0
for i in a:
    if i[0] in g:
        gct += 1
    elif i[0] in sg:
        sgct += 1
print(f'Всего слов: {len(a)}\nвсего слов начинающихся на гласную: {gct}\nвсего слов начинающихся на согласную: {sgct}')
