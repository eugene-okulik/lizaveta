class Book:
    page_material = 'paper'
    text_presence = True

    def __init__(self, title, author, page_number, ISBN):
        self.title = title
        self.author = author
        self.page_number = page_number
        self.ISBN = ISBN
        self.reserved = False


book_1 = Book('The Idiot', 'Fyodor Dostoevsky', 656, '978-0-14-044792-8')
book_2 = Book('1984', 'George Orwell', 328, '978-0-452-28423-4')
book_3 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 180, '978-0-7432-7356-5')
book_4 = Book('Pride and Prejudice', 'Jane Austen', 432, '978-0-14-143951-8')
book_5 = Book('Fahrenheit 451', 'Ray Bradbury', 256, '978-1-4516-7331-9')
book_5.reserved = True

books = [book_1, book_2, book_3, book_4, book_5]
for book in books:
    if book.reserved:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_number}, '
              f'материал: {book.page_material}, зарезервирована')
    else:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_number}, '
              f'материал: {book.page_material}')


class Textbook(Book):
    def __init__(self, title, author, page_number, ISBN, subject, grade, tasks):
        super().__init__(title, author, page_number, ISBN)
        self.subject = subject
        self.grade = grade
        self.tasks = tasks


textbook_1 = Textbook('Algebra Essentials', 'John Smith', 200, '978-1-11-111111-1',
                      'Mathematics', '9', True)
textbook_2 = Textbook('World History', 'Anna Brown', 340, '978-2-22-222222-2',
                      'History', '7', False)
textbook_2.reserved = True
textbook_3 = Textbook('Physical Geography', 'Mark Green', 280, '978-3-33-333333-3',
                      'Geography', '8', True)

textbooks = [textbook_1, textbook_2, textbook_3]
for textbook in textbooks:
    if textbook.reserved:
        print(f'Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.page_number}, '
              f'предмет: {textbook.subject}, класс: {textbook.grade}, зарезервирована')
    else:
        print(f'Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.page_number}, '
              f'предмет: {textbook.subject}, класс: {textbook.grade}')
