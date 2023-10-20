def archiver(text: str) -> str:
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
    if not text:
        return ''
    # Создаем пустую строку и инициализируем пер-ую sim
    empty_text = ''
    sim = 0
    # Пока не достигнет входной строки
    while sim < len(text):
        # Получаем текущий символ
        char = text[sim]
        # Увеличиваем индекс, чтобы перейти к другому символу
        sim += 1
        # Инициализируем перем-ую для хранения повторяющихся символов
        replay = ''
        # следующий текст является цифрой для кол-ва повторений
        while sim < len(text) and text[sim].isdigit():
            # Добавляем цифры
            replay += text[sim]
            # Переходим к след. символу
            sim += 1
        if replay:
            empty_text += char * int(replay)
        # Добавляем повторяющиеся символы в строку
    return empty_text
