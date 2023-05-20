# ABC for classes that provide the __iter__() and __next__() methods.
# __iter__(): This method returns the iterator object itself.
# __next__(): This method is responsible for returning the next element in the iterator.
from collections.abc import Iterator

class Book:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    # 此處將返回一個 Iterator 實例。
    def iterator(self):
        return BookIterator(self.books)

class BookIterator(Iterator):
    def __init__(self, books):
        # 當下遍歷到的索引
        self.index = 0
        self.books = books

    def __next__(self):
        try:
            # 儲存回傳值
            book = self.books[self.index]
        except IndexError:
            # 已經沒有下一個元素
            raise StopIteration()
        
        # 索引遞增
        self.index += 1

        # 回傳元素
        return book

def main():
    bookshelf = Bookshelf()

    bookshelf.add_book(Book("Book 1"))
    bookshelf.add_book(Book("Book 2"))
    bookshelf.add_book(Book("Book 3"))

    iterator = bookshelf.iterator()
    for book in iterator:
        print(book.get_title())

if __name__ == "__main__":
    main()

# 將遍歷方式與集合本身解耦，
# 提升代碼維護性，
# 當需要新的遍歷方式時，
# 只需要增加新的迭代器即可。
