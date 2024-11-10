#Лямбда функции
def book_list(books, func):
    for book in books:
        print(func(book))
books = ['книга','журнал','Git. Практическое руководство']
book_list(books, lambda book: book.upper() + ' - прочитано')