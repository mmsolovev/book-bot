import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}
signs = ',.!:;?'


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text: str = text[start:(start + size)][::-1]
    page: str = ''
    for i, j in enumerate(text):
        if str(j) in signs and text[i + 1] not in signs and text[i - 1] not in signs:
            page: str = text[i:][::-1]
            break
    return page, len(page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
