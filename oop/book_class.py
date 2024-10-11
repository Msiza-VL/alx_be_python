class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"
from book_class import Book
def main():
    # Creation
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstration
    print(my_book)  # Expected to use __str__

    # Demonstration
    print(repr(my_book))  # Expected to use __repr__

    # Deleting
    del my_book

if __name__ == "__main__":
    main()