def reserve_text(text):
    
    '''Функція слугує для зміни порядку літер у словах певного речення (параметр text) на протилежний.
    Так звані "нелітери" зберігають своє місце в кожному слові речення.'''
    
    l = text.split()    # початковий список слів, який слугує для зберігання кількості символів в словах
    l_new = text.split()    # список слів, з яким будуть проводитись дії    
    not_letters = [dict() for s in l]   # кожному слову відповідає словник з інформацією про символи "нелітери"
    
    # наповнення словників і прибирання "нелітер" у словах списку l_new
    for i, s in enumerate(l_new):
        for j, symbol in enumerate(s):
            if not symbol.isalpha():
                l_new[i] = s[ : j] + s[j + 1 : ]
                not_letters[i][j] = symbol
    
    # формування результату роботи функції
    l_new = [s[ : : -1] for s in l_new]
    result = str()
    for i, s in enumerate(l_new):
        for j in range(len(l[i])):
            not_letter = not_letters[i].get(j)
            if not_letter:
                result += not_letter
            else:
                if s[j].isalpha():
                    result += s[j]
        result += ' '
    
    return result

if __name__ == '__main__':
    while True:
        print(reserve_text(input('Введіть речення: ')))