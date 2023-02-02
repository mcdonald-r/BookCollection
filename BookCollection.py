#BookCollection.py

from BookCollectionNode import BookCollectionNode
from Book import Book

class BookCollection(Book, BookCollectionNode):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0

        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False 

        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        current = self.head
        output = ""

        while current != None:
            if author.upper() in str(current.getData().getBookDetails()).upper():
                output += str(current.getData().getBookDetails()) + "\n"
                current = current.getNext()
            else:
                current = current.getNext()
        return output

    def getAllBooksInCollection(self):
        current = self.head
        output = ""

        while current != None:
            output += str(current.getData().getBookDetails()) + "\n"
            current = current.getNext()
        return output

    def removeAuthor(self, author):
        current = self.head
        bookCount = self.getNumberOfBooks()

        if current == None:
            return

        previous = None
        for i in range(bookCount):
            if author.upper() in str(current.getData().getBookDetails()).upper():
                if previous == None:
                    self.head = current.getNext()
                    current = current.getNext()
                else:
                    previous.setNext(current.getNext())
                    current = current.getNext()
            else:
                previous = current
                current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        else:
            temp = bookNode.getData().getBookDetails()
            if title.upper() in str(temp).upper():
                return True
            else:
                temp = bookNode.getNext()
                return self.recursiveSearchTitle(title, temp)
                