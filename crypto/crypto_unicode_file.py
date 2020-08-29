file = open('output.txt', 'w')

a = []
n = 0

def crypto(uni):
    ''' Получает номер символа по таблице Unicode. '''
    for j in uni:
        a.append(ord(j))
    print('List of elements in Unicode:', a, sep='\n')
    return a

for i in open('input.txt'):
    # Переводит по таблице Unicode.
    crypto(i)
    # Для каждого элемента в файле через пробел.
    c = i.split()
    # Удаляет элемент с индексом 0.
    c.pop(0)
    # Помещает по индексу 0 элемент списка.
    c.insert(0, a[n])
    # По бокам каждого элемента 'ничего' не добавлять и присоединить элемент из открытого файла.
    c = ' '.join(map(str, a))
    # Записывает в новый файл.
    file.write(c)
    # Переход по индексу к следующему элементу.
    n += 1
    print('Recorded in a new file.', 'Processing...', 'Completed!', sep='\n', end='')

file.close()