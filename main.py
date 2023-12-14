def title(s):
    chars = []
    # Перевод символа в число из таблицы ASCII
    ascii_codes = [ord(char) for char in s]
    # Перевод числа обратно в символ и, если предыдущее число не является алфавитной букво, то текущий символ
    # становится заглавным
    for i in range(len(ascii_codes)):
        if i >= 0 and 'a' <= chr(ascii_codes[i]) <= 'z' \
                and not chr(ascii_codes[i - 1]).isalpha(): # Проверка, что символ строчный и явяется буквой
            # английского алфавита
            code = ascii_codes[i] - 32
            character = chr(code)
        elif i >= 0 and 'а' <= chr(ascii_codes[i]) <= 'я' \
                and not chr(ascii_codes[i - 1]).isalpha():  # Проверка, что символ строчный и явяется буквой русского
            # алфивита
            code = ascii_codes[i] - 32
            character = chr(code)
        else:
            character = chr(ascii_codes[i])
        chars.append(character)

    return ''.join(chars)

s = "this_code   make All words@with/apper    case on,english. а Теперь   и  на:русском  "
result = title(s)
print(result)