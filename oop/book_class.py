class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")
    def __str__(self) -> str:
        """String representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self) -> str:
        """Official representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstration
    print(my_book)  
    
    # Demonstration
    print(repr(my_book)) 

    # Deleting
    del my_book

if __name__ == "__main__":
    main()