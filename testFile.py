#testFile.py

from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode

def test_Book():
    b1 = Book("Less", "Greer, Andrew", 2018)

    assert b1.getAuthor() == "Greer, Andrew"
    assert b1.getTitle() == "Less"
    assert b1.getYear() == 2018
    assert b1.getBookDetails() == "Title: Less, Author: Greer, Andrew, Year: 2018"

    b2 = Book()
    assert b2.getAuthor() == ""
    assert b2.getTitle() == ""
    assert b2.getYear() == None
    assert b2.getBookDetails() == "Title: , Author: , Year: None"

def test_BookCollection():
    b0 = Book("Verity", "Hoover, Colleen", 2018)
    b1 = Book("No Plan B", "Child, Lee", 2022)
    b2 = Book("It Ends With Us", "Hoover, Colleen", 2016)
    b3 = Book()
    b4 = Book("Wonder", "Palacio, R. J.", 2012)

    bc = BookCollection()

    assert bc.isEmpty() == True
    assert bc.getNumberOfBooks() == 0
    
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.insertBook(b4)

    assert bc.getAllBooksInCollection() == "Title: , Author: , Year: None\n" \
    "Title: No Plan B, Author: Child, Lee, Year: 2022\n" \
    "Title: It Ends With Us, Author: Hoover, Colleen, Year: 2016\n" \
    "Title: Verity, Author: Hoover, Colleen, Year: 2018\n" \
    "Title: Wonder, Author: Palacio, R. J., Year: 2012\n"

    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 5

    assert bc.getBooksByAuthor("colleen") == "Title: It Ends With Us, Author: Hoover, Colleen, Year: 2016\n" \
    "Title: Verity, Author: Hoover, Colleen, Year: 2018\n" 
    assert bc.getBooksByAuthor("Joey") == ''

    bc.removeAuthor("COLLEEN")

    assert bc.getAllBooksInCollection() == "Title: , Author: , Year: None\n" \
    "Title: No Plan B, Author: Child, Lee, Year: 2022\n" \
    "Title: Wonder, Author: Palacio, R. J., Year: 2012\n"

    assert bc.getNumberOfBooks() == 3

    assert bc.recursiveSearchTitle("", bc.head) == True
    assert bc.recursiveSearchTitle("WONDER", bc.head) == True
    assert bc.recursiveSearchTitle("Nothing", bc.head) == False
    

def test_BookCollectionNode():
    b0 = Book("Verity", "Hoover, Colleen", 2018)
    b1 = Book("No Plan B", "Child, Lee", 2022)
    b3 = Book()

    bcn = BookCollectionNode(b0)
    

    assert bcn.getData() == b0
    assert bcn.getNext() == None

    bcn.setNext(b1)
    assert bcn.getNext() == b1

    bcn2 = BookCollectionNode(b1)

    assert bcn2.getData() == b1
    
    bcn2.setNext(b3)
    assert bcn2.getNext() == b3
    