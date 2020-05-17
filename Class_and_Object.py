"""
Python Classes and Objects || Python Tutorial || Learn Python Programming
ref: https://www.youtube.com/watch?v=apACNr7DC_s&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=23
"""
import datetime

# When creating a class, we need to at least put in a line
# # Example 1
# user1 = User()  # user1 is an "instance" of User
#                 # user1 is an "object" of User
#
# # to attach data to an object, we type the object, dot, followed by a variable
# # since the "first_name" and "last_name" store the data of an object, we call them "field"
# # should NOT capitalize the name of field,
# # ... lowercase with words separated by underscores as necessary to improve readability
# user1.first_name = "Dave"
# user1.last_name = "Stephen"
# user1.age = 37
#
# user2 = User()
# user2.first_name = "Frank"
# user2.last_name = "Poole"
# user2.favorite_book = "Sex in the city"



# Example 2:
class User:
    """ This is a help file for Class User"""   # to create a help file, we use triple quote (""") inside Class
    def __init__(self, name, DOB):              # the very first function we create in Class
        self.name = name
        self.DOB = DOB
        # Extract first and last names
        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years"""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.DOB[0:4])
        mm = int(self.DOB[4:6])
        dd = int(self.DOB[-2:-1])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days        # the difference between today & dob create a time delta object
        age_in_years = age_in_days / 365        # time delta object has attribute called "days"
        return int(age_in_years)

user = User("Dave Bowman", "19881231")

help(User)



# # Example 3
# class Robot:
#     def __init__(self, name, weight, color):
#         self.name = name
#         self.weight = weight
#         self.color = color
#
#     def introduce_self(self):
#         print("My name is " + self.name)
#
#
# # r1 = Robot()
# # r1.name = "Tom"
# # r1.weight = 30
# # r1.color = 'red'
# #
# # r2 = Robot()
# # r2.name = 'Jerry'
# # r2.weight = 50
# # r2.color = 'blue'
#
# r1 = Robot("Tom", 40, "red")
# r2 = Robot("Jenny", 100, "green")
#
# r1.introduce_self()


# # Example 3
# class Student:
#     def __init__(self, name, major, gpa, is_on_probation):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation
#
#
# student1 = Student("Jim", "Biological sciences", 3.89, True)
#
# print(student1.name)
