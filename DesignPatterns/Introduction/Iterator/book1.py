# 書籍類別: 涵蓋書籍資訊。
class Book:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title


# 書架類: 實作書籍管理。
class Bookshelf:
    def __init__(self):
        self.books = []

    # 上架書籍。
    def add_book(self, book):
        self.books.append(book)

    # 獲取書籍。
    def get_books(self):
        return self.books


if __name__ == "__main__":
    bookshelf = Bookshelf()

    bookshelf.add_book(Book("Book 1"))
    bookshelf.add_book(Book("Book 2"))
    bookshelf.add_book(Book("Book 3"))

    books = bookshelf.get_books()

    for book in books:
        print(book.get_title())

# 這是一個不符合開閉原則的設計，
# 如果需要修改遍歷的模式，
# 就需要修改現有的代碼，
# 假設需求為排序需依照書籍標題排序，
# 此時可能需要修改 get_books() 方法，
# 而且還有機率導致現有客戶端不相容問題。
