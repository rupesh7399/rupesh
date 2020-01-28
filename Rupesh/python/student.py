#---In this example , you have to take number of students as input , then ask marks for three subjects as ‘Physics’, ‘Maths’, ‘History’, if the total marks for any student is less 120 then print he failed, or else say passed.
n = int(input("Enter a number of student"))
data = {}
language = ('Physics','Maths','History')
for i in range(0 , n):
    name = input('Enter the Name of student %d:' %(i+1))
    marks = []
    for x in language:
        marks.append(int(input("Enter the marks of %s:" % x)))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("%s 's total marks %d" % (x, total))
    if total < 120:
        print("%s failed :(" % x)
    else: 
        print("%s passed :)" % x)