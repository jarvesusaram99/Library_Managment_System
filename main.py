class Library:
    no_of_books = 1
    donate_book_name = None
    lend_book = None
    books_name = None
    return_book = None
    already_issued = None
    my_dict = None

    def __init__(self, no_of_books, library_name):
        self.no_of_books = no_of_books
        self.libraryname = library_name
        self.mydict = {}

    def display_books(self):
        for books in self.no_of_books:
              print(books)

    def lend_book_fun(self, lend_book , name):
        self.lend_book = lend_book
        self.name = name

        if lend_book not in self.mydict.keys():
              self.mydict.update({lend_book : name})
              print("Library database activated")
              try:
                self.no_of_books.remove(lend_book)
              except ValueError as e:
                print(e)
                print(f"Book is not in the library")
              # finally:
              #   print("Library database activated")
        elif lend_book not in self.no_of_books:
            print(f"Book is already being by {self.mydict[lend_book]} ")
        else:
            print("book is already being by " , self.mydict[lend_book])


        # self.my_dict = mydict
        # if lend_book in self.no_of_books:
        #     self.no_of_books.remove(lend_book)
        #     print(f"Book lend succefully to {self.name} And book name is {self.lend_book}")
        #     self.my_dict.append({self.lend_book: self.name})
        # elif lend_book in self.my_dict:
        #     print(f"Book is alredy lend by {self.my_dict}")
        #     print("Please lend another book")


    def add_book(self, donate_book_name):
        # self.donate_book_name = donate_book_name
        if donate_book_name not in self.no_of_books:
            self.no_of_books.append(donate_book_name)
            print(f"{donate_book_name} added in the library . Thanks You")
        else:

            print(f"{donate_book_name} is already in the library. Please add in the another book")

    def return_book_fun(self, return_book):
        if return_book not in self.no_of_books and return_book in self.mydict.keys():
                self.return_book = return_book
                self.no_of_books.append(return_book)
                self.mydict.pop(return_book)
                print(f"{return_book} returned sucessfully")
        else:
            print(f"{return_book} book not issued earlier")

    # def already_lend_book_fun(self):

if __name__ == '__main__':

        print("--------------Hello , welcome in Jarves Lirbrary------------")
        JarvesLibrary = Library(["C++", "Java", "Python", "C#" , "Physics" ], "Jarves Library")
        n = 1
        while n == 1:

            print("Choose your option")
            print("Press 1 : Display All books ")
            print("Press 2 : Lend any book ")
            print("Press 3 : Add book")
            print("Press 4 : Return your book ")

            user_input = (input())
            if user_input == "1":
                JarvesLibrary.display_books()
            elif user_input == "2":
                lend_book_name = input("Enter the book name\n")
                your_name = input("Enter your name\n")
                Mydict = {lend_book_name: your_name}
                JarvesLibrary.lend_book_fun(lend_book_name, your_name)

            elif user_input == "3":
                donate_book = input("Enter donate book name\n")
                JarvesLibrary.add_book(donate_book)

            elif user_input == "4":
                return_book = input("Enter return book name\n")
                JarvesLibrary.return_book_fun(return_book)
            else:
                print("Wrong input")

        n = n + 1





