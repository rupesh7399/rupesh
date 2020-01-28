class Student(object):

    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print('A Student object is created.')

    def print_details(self):
        print("Name:",self.name)
        print("Branch:", self.branch)
        print("year:", self.year)
    
std1 = Student(
        input("Enter a name:"),
        input("Enter a branch:"),
        input("Enter a Year:")
    )
std1.print_details()
