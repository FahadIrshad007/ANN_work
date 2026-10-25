# Task : 01
name = "Fahad Irshad"
rollno = "FA23-BAI-014"
cgpa = 3.40
print("=======================================================================")
print('Name',name, '| d-type', type(name))
print('Rollno',rollno, '| d-type', type(rollno))
print('CGPA',cgpa, '| d-type', type(cgpa))
print("=======================================================================")

marks1 = 80
marks2= 77
print(f"Before upadting: \nmarks1: {marks1}\nmarks2: {marks2}")
marks1+=5
marks2-=3
print(f"After upadting: \nmarks1: {marks1}\nmarks2: {marks2}")
print("=======================================================================")
print(marks1 == marks2)
print(marks1 > marks2)
print("=======================================================================")
print(f"Before Swapping: \nmarks1: {marks1}\nmarks2: {marks2}")
marks1 ,marks2 = marks2 , marks1
print(f"After Swaping: \nmarks1: {marks1}\nmarks2: {marks2}")
print("=======================================================================")

# Task : 02
favorite_subjects = ["AI", "DSA","IS"]
favorite_subjects.append("ANN")
favorite_subjects.insert(0,"Robotics")
print(favorite_subjects)
print("=======================================================================")
favorite_subjects.remove('DSA')
favorite_subjects.pop()
print(favorite_subjects)
print("=======================================================================")

favorite_subjects.sort()
print('Sorted List: ',favorite_subjects, '\nLength : ',len(favorite_subjects))

print("=======================================================================")

# Task : 03
weekdays = ('saturday','sunday','monday','tuesday','wednesday')
# weekdays[1]='friday'
# print(weekdays)
subject_credits ={
    'AI':3,
    'DSA':3,
    'PF':4
}
print("=======================================================================")
print(subject_credits)
subject_credits['DSA'] = 4
subject_credits['Ecommerce'] = 2
print(subject_credits)
print("=======================================================================")

# Task : 04
numbers = list()
for i in range(1,16):
    numbers.append(i)

print(numbers)
print('First 4 : ',numbers[:4],'\nLast 4: ',numbers[-4:])
print("=======================================================================")
print('Every Third : ',numbers[::3])
print('Reversed : ',numbers[::-1])
print("=======================================================================")

# Task : 05
my_name = "Abdulmoiz Abbasi"
first_name = my_name.split()[0]
last_name  = my_name.split()[1]
print(f"My first name is {first_name} and my last name is {last_name}.")
print("=======================================================================")
vowels = "aeiou"
vowels_count= 0
print('Vowels Found in my name :')        
for c in my_name:
    if c in vowels:
        vowels_count+=1
        print(c)
print("=======================================================================")        
print(f'Totel Vowels in my name : {vowels_count}')        
print("=======================================================================")
upper = my_name.upper()
lower = my_name.lower()
print(upper)
print(lower)
print(upper == lower)
print("=======================================================================")

# Task : 06
marks = 80
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")    
elif marks >= 60:
    print("Grade D")    
else:
    print("Grade F")    
print("=======================================================================")
n = 7
if n < 0:
    print ('Number is negative')    
elif n > 0:    
    print ('Number is positive')    
else:
    print ('Number is zero')        
print("=======================================================================")

# Task : 07
for i in range(1, 31):

    if i % 4 == 0:

        continue

    print(i)

print("=======================================================================")


for i in range(1, 51):

    if i > 20:

        break

    print(i)

print("=======================================================================")

number = 7

i = 1

while i <= 10:

    print(number, "x", i, "=", number * i)

    i += 1

print("=======================================================================")

sum_even = 0

for i in range(1, 101):

    if i % 2 == 0:

        sum_even += i

print("Sum of even numbers =", sum_even)

print("=======================================================================")


# Task : 08
def calculate_area(length, width=1):

    return length * width

print("Area =", calculate_area(10, 5))

print("Area =", calculate_area(10))

area = calculate_area(8, 4)

print("Stored area =", area)

print("=======================================================================")

def is_even(number):

    if number % 2 == 0:

        return True

    else:

        return False


print(is_even(10))

print(is_even(7))

print("=======================================================================")

def add_item(my_list):

    print("Before adding item:", my_list)

    my_list.append("Orange")

    print("After adding item:", my_list)


fruits = ["Apple", "Banana"]

print("Before function call:", fruits)

add_item(fruits)

print("After function call:", fruits)

print("=======================================================================")


# Task : 09

class Course:

    def __init__(self, course_name, credit_hours):

        self.course_name = course_name

        self.credit_hours = credit_hours


    def display_info(self):

        print("Course Name:", self.course_name)

        print("Credit Hours:", self.credit_hours)

course1 = Course("Python Programming", 3)

course2 = Course("Database Systems", 4)

course1.display_info()

print("-----------------------------------------------------------------------")

course2.display_info()

print("=======================================================================")

class LabCourse(Course):

    def __init__(self, course_name, credit_hours, lab_hours):

        super().__init__(course_name, credit_hours)

        self.lab_hours = lab_hours

    def display_info(self):

        print("Course Name:", self.course_name)

        print("Credit Hours:", self.credit_hours)

        print("Lab Hours:", self.lab_hours)


lab_course = LabCourse("Programming Lab", 3, 2)

lab_course.display_info()

print("=======================================================================")
