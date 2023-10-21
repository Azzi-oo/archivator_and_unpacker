def archiver(text: str) -> str:
    # Проверка на пустую строку
    if not text:
        return ''
    compressed_text = ''
    # Инициализируем счетчик повторяющихся символов
    count = 1

    # Проходим по каждому символу в строке
    for i in range(1, len(text)):
        # Если символ совпадает с предыдущим, то увеличиваем на 1
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Если текущий символ отличается от предыдущего
            # добавляем предыдущий символ и сбрасываем счетчик
            compressed_text += text[i - 1] + str(count)
            count = 1
    # Добавляем последний символ и его кол-во
    # в сжатую строку и возвращаем сжатую строку
    compressed_text += text[-1] + str(count)
    return compressed_text


def unpacker(text: str) -> str:
    # Если пустая строка, то вернуть пустую строку
    if not text:
        return ''
    # Создаю пустую строку для распакованного текста
    empty_text = ''
    # В цикле перебираю по 2 символа
    for i in range(0, len(text), 2):
        # Получаю текущий символ
        symbol = text[i]
        # Получаю кол-во повторений
        replay = text[i + 1]
        # Добавляю букву, в распакованный текст
        empty_text += symbol * int(replay)
    # Возвращаю пустой текст
    return empty_text
