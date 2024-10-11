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
import os
import subprocess
from book_class import Book

def check_file(file_path):
    """Check if a file exists and is not empty."""
    if not os.path.isfile(file_path):
        return False
    return os.path.getsize(file_path) > 0

# Check files
assert check_file('book_class.py'), "book_class.py does not exist or is empty"
assert check_file('main.py'), "main.py does not exist or is empty"

# Check for successful creation
try:
    my_book = Book("1984", "George Orwell", 1949)
except Exception as e:
    print(f"Failed to create Book class: {e}")

# Check for initialization
try:
    import os
    import sys
except ImportError as e:
    print(f"Import error: {e}")

# Testing
def test_magic_methods():
    book = Book("1984", "George Orwell", 1949)
    assert str(book) == "1984 by George Orwell, published in 1949", "__str__ method not working correctly"
    assert repr(book) == "Book('1984', 'George Orwell', 1949)", "__repr__ method not working correctly"

test_magic_methods()

# Checks for output
def check_output():
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    expected_output = "1984 by George Orwell, published in 1949\nBook('1984', 'George Orwell', 1949)\nDeleting 1984\n"
    assert result.stdout == expected_output, f"Output was not as expected: {result.stdout}"

check_output()

print("All checks passed successfully!")