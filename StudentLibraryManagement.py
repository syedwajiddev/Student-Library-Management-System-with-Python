class Library:

    def __init__(self, listofBooks):
        self.books = listofBooks
    
    def displayAvailableBooks(self):
        print("-----------------------------------------")
        print("Book present in this library")

        for book in self.books:
            print("\t" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it in 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is already issued by someone, please keep visiting")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for Returning the Book, Hope you enjoyed.")

class Student:
    def requestBook(self):
        self.books = input("Enter the name of the book you want to borrow : ")
        return self.books
    
    def returnBook(self):
        self.books = input("Enter the name of the book you want to return : ")
        return self.books
        

if __name__ == '__main__':
    centralLibrary = Library(["1. Data Structure", "2. Django", "3. SQL Database", "4. Python Programming", "5. Machine Learning", "6. UI UX Designing"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomMsg = ''' ------------ Welcome to Mehran Library ---------------
                    Please Select Choose from given below : 
                    1. Listening all the books
                    2. Request a book
                    3. Return a book
                    4. Exit the Library
                    '''
        a = int(input("Enter a Choice : "))   

        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a == 2:
            centralLibrary.borrowBook()

        elif a == 3:
            centralLibrary.returnBook()

        elif a == 4:
            print("Thanks for using our Library System")
            exit()

        else:
            print("Invalid Choice")
    
    print(welcomMsg)



    