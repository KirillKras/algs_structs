#Функция хеширования


def my_hash(txt):
    len_txt = len(txt)
    result = 0
    for sub_len in range(1, len_txt):
        left = 0
        right = left + sub_len - 1
        while right < len_txt:
            result += 1
            left += 1
            right = left + sub_len - 1
    return result


txt = input('Введите текст: ')

print(my_hash(txt))