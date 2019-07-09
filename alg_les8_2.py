#Функция хеширования


def my_hash(txt):
    len_txt = len(txt)
    result = set()
    for sub_len in range(1, len_txt):
        left = 0
        right = left + sub_len - 1
        while right < len_txt:
            sub_txt = txt[left:right + 1]
            print(sub_txt)
            result.add(sub_txt)
            left += 1
            right = left + sub_len - 1
    return len(result)


txt = input('Введите текст: ')

print(my_hash(txt))