# This program demonstrates Object-Oriented Programming using a Library class.
# It allows adding books to the library and displays the total number of books along with their names.


class Library:
  def __init__(self):
    self.books = []
    self.noOfBooks = 0
  def addBooks(self, book):
    self.books.append(book)
    self.noOfBooks = len(self.books)
  def showInfo(self):
    print(f"The library has {self.noOfBooks} books. The following books are:")
    for book in self.books:
      print(book)
l1 = Library()
l1.addBooks("Harry Potter")
l1.addBooks("Fault")
l1.addBooks("It ends with us")
l1.addBooks("The Palace of Illusions")
l1.showInfo()
