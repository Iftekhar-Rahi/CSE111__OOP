class Student:
    def __init__(self,name,id,dept="CSE"):
        self.name=name
        self.id=id
        self.dept=dept
        self.hour=0
    def dailyEffort(self,hour):
        self.hour = hour
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.hour} hour(s)")
        if self.hour<=2:
            print('Suggestion: Should give more effort!')
        elif self.hour<=4:
            print('Suggestion: Keep up the good work!')
        else:
            print('Suggestion: Excellent! Now motivate others.')
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
