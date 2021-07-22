#پروژه پایانی- دفترچه تلفن
class PhoneBook:

    def __init__(self):
        self.names = []
        self.numbers = []
        self.phonebk = []

    # قسمت اول تمرین- اضافه کردن به دفترچه تلفن
    def addContact(self, name, number):
        self.names.append(name)
        self.numbers.append(number)
        self.phonebk.append([name, number])
        print("Contact added successfully")

    # قسمت دوم تمرین: هر اسمی که دادم شماره را به عنوان خروجی بده
    def searchContact(self,name):
            if name in self.names:
                list = []
                for a,b in enumerate(self.names):
                    if b == name:
                        list.append(a)

                for c in list:
                    print("name:",self.names[c], "\tphone number:", self.numbers[c], "\n")
            else:
                print("Sory, contact not found")


    # قسمت سوم تمرین: لیست افراد در دفترچه تلفن رو نمایش بده
    def ContactShow(self):
        for cname in self.phonebk:
            print("contact name: " , cname[0], "\tphone number: ", cname[1])


#.......main.............
if __name__ == "__main__":

    Book = PhoneBook()

    while True:
        operation = input("Welcome to Phonebook app, enter a operation:\
 add, search, show\n")

        if operation == "add":
            name = input("Enter Name:\n")
            phone_number = input("Enter number:\n")
            Book.addContact(name,phone_number)

        elif operation == "search":
            search_name = input("Please enter the name to search\n")
            Book.searchContact(name)

        elif operation == "show":
            print("list of your contactes:\n")
            Book.ContactShow()

        else:
            break
