class Author:
    def __init__(self,name):
        self.name=name
        print(f"Author Name:  {self.name}")
        print("--------")

    def addBooks(self,*args):
        print("List of Books:")
        for i in args:
            print(i)

auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()