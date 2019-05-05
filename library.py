class LIBRARY:
    def __init__(self,bk_list,name):
        self.bok_list=bk_list
        self.name=name
        self.lbry_dict={}

    def Display_book(self):
        print(f"these are following books in our library :{self.name}")
        for book in self.bok_list:
            print(book)
    def issue(self,user,name):
        if book not in self.lbry_dict.keys():
            self.lbry_dict.update({book:user})
            print("dictonary data is updated")
        else:
            print(f"book is already being used by{self.lbry_dict[book]}")

    def add_book(self,book):
        self.bok_list.append(book)
        print("book has been added to book list")

    def returnd(self,book):
        if book not in self.bok_list:
            print(f"book is not present  in book list")

        else:

            self.bok_list.remove(book)

if __name__ == '__main__':
    Atul=LIBRARY(['python','science','math','c++','algorithm'],"GNDIT")
    while(True):
        print(f"Welcome to {Atul.name} library.\n Enter your choice")
        print("1.Display the books")
        print("2.issue the book")
        print("3.Add the book")
        print("4.return the book")
        user_choice=int(input())
        if user_choice==1:
            Atul.Display_book()

        elif user_choice==2:
            book=print("Enter the book name that you want to issue")
            user=input("enter your name")
            Atul.issue(user,book)

        elif user_choice==3:
            book=input("enter the book name that you want to add")
            Atul.add_book(book)

        elif user_choice==4:
            book=input("enter the book name that you want to returned ")
            Atul.returnd(book)
        else:
            print("Enter a valid choice")

        user_choice2=" "

        print("Enter Q to exit and C to continue")
        while(user_choice2!="q" and user_choice2!="c"):

            user_choice2=input("enter your choice")

            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue

            else:
                print("Enter a valid choice")






