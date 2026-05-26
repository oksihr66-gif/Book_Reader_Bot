def _get_part_text(text: str, start, page_size: int):
    operators = '.,:!?;'
    end = start + page_size
    if end > len(text):
        return text[start:], len(text[start:])
    while end:
        if text[end-1] in operators and (text[end]==' ' or text[end]=='\n'):
            result = text[start:end]
            return result, len(result)
        else:
            end = end-1

def prepare_book(path, page_size=1050):
    book = {}

    with open(path, 'r', encoding='utf-8') as file:
        file = file.read()
        start = 0
        num = 1
        for _ in file:
            key = _get_part_text(file, start, page_size)
            if key[0]:
                book[num] = key[0].strip()
                start += key[1]
                num +=1


    return book



