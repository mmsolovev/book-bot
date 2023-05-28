import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}
signs = ',.!:;?'
text = 'Раз. Два. Три. Четыре. Пять. Прием!'


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    n: str = text[start:(start + size)][::-1]
    x: str = ''
    for i, j in enumerate(n):
        if str(j) in signs and n[i + 1] not in signs and n[i - 1] not in signs:
            x: str = n[i:][::-1]
            break
    return x, len(x)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
# prepare_book(os.path.join(os.getcwd(), BOOK_PATH))

print(*_get_part_text(text, 5, 9), sep='\n')
