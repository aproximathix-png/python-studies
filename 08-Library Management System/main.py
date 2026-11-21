import json
class Book: 
   
    def __init__(self, name,author,borrowed = False):
        self._borrowed = False
        self.name = name
        self.author = author
    def display_info(self):
       print(self.name,self.author,self._borrowed)
    def borrow_book(self) : 
        if self._borrowed == False : 
            self._borrowed = True
            print("you have borrowed the book")
        else:
            print("arldy borrowed")
    def return_book(self) : 
        if self._borrowed == True : 
            self._borrowed = False   
        else : 
            print("the book wasnt borrowed")
    @property
    def borrowed(self):
        return  self._borrowed 

    def to_dict(self):
     book = {
         "name":self.name,
         "author": self.author,
         "borrowed" : self.borrowed
     }
     return book
class Library:

    def  __init__(self,):
        self.books =  []
    def add_book(self,book) :
        self.books.append(book)
        print("book added")
    def display_book(self):
        if self.books == []:
            print("its empty")
        else : 
            for books in self.books:
               books.display_info()
    def search_book(self):
        print("wich book are we searching for")
        found = False  
        search = input()                                                                                                                            
        for book in self.books:                                                                                                            
            if search == book.name:
                print("book found")
                book.display_info()
                found = True
        if not found  :
                print("book not found")


    def borrow_book(self,title): 
        found = False
        for book in self.books:
           if title == book.name:
               book.borrow_book()
               found = True
        if not found:
               print("book not found")
                
    def return_book(self,title):
        found = False
        for book in self.books:
            if title == book.name:
                book.return_book()
                found = True
        if not found:
            print("book not found")
    def to_dict(self):
      book_data = []
      for book in self.books:
            book_data.append(book.to_dict())
      return book_data
    def save_to_file(self):
        with open("library.json", "w") as file:
            json.dump(self.to_dict(), file)


    def load_from_file(self):
        try:
            with open("library.json", "r") as r:
                books_data = json.load(r)

            for book_data in books_data:
                new_book = Book(
                    book_data["name"],
                    book_data["author"],
                    book_data["borrowed"]
                )
                self.add_book(new_book)

        except FileNotFoundError:
            print("No saved library found. Starting with an empty library.")



Library = Library()       
Library.load_from_file()  
def menu():
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1-add a book")
    print("2-search for a book")
    print("3-borrow")
    print("4-return")
    print("5-display")
    print("6-save")
    print("7-exit")
    validiation = False
    while validiation == False :
        try:
      
            choice = int(input("you chose :"))
            if choice in  {1, 2, 3, 4, 5, 6,7}:
                validiation = True
            else:
                print("wrong number")
                
        except ValueError:
            print("The value has wrong format")
                            
        
    return choice 


while True:
    choice = menu()

    if choice == 1:
        print("which book do you want to add, author and title pls")
        title = input("title:")
        author = input("author:")
        book = Book(title, author)
        Library.add_book(book)

    elif choice == 2:
        if not Library.books:
            print("nothing to see here")
        else :
            Library.search_book()
            


    elif choice == 3:
        if not Library.books:
            print("nothing to see here")
        else:
            print("wich book do you want to borrow?")
            title = input("title : ")
            Library.borrow_book(title)

    elif choice == 4:
        if not Library.books:
                    print("nothing to see here")
        else :  
            print("which book do you want to return")
            title = input("title ;")
            Library.return_book(title)

    elif choice == 5:
        Library.display_book()
    elif choice == 6:
        Library.save_to_file()
        print("saved!")

    elif choice == 7:
        Library.save_to_file()
        break
        
    