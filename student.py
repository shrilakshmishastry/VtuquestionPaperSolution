##5b dec 2018
class Student(object):
    """docstring forStudent."""
    usn = ""
    marks=dict()

    def __init__(self, usn,mark1,mark2,mark3):
        self.usn = usn
        self.marks["mark1"] = mark1
        self.marks["mark2"] = mark2
        self.marks["mark3"] = mark3
    def find_max_and_min(self)    :
        print("usn",self.usn)
        print("your maximum max",max(self.marks["mark1"],self.marks["mark2"],self.marks["mark3"]))
        print("your minimum max",min(self.marks["mark1"],self.marks["mark2"],self.marks["mark3"]))

print("how many Student s info you want to upload")
n = int(input())
for i in range(0,n):
    print("Student info")
    usn = input("Enter your usn")
    mark1 = int(input("enter your first mark"))
    mark2 = int(input("enter your second mark"))
    mark3 = int(input("enter your third mark"))

    stu = Student(usn,mark1,mark2,mark3)
    stu.find_max_and_min()
