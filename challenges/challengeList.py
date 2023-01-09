#!/bin/user/python3

"""
Challenge Lists, Input, Concatenation
"""
import random

def main():
    #creating a list of random things
    wordbank= ["indentation", "spaces"]

    #creating a list of students
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    #adding 4 to the list of wordbank
    wordbank.append(4)

    #asking a number between 0 to 20
    num = 0
    max = len(tlgstudents)-1

    while True:
        try:
            num = int(input(f"Please choose a number between 1 and {max}\n"))
        except ValueError:
            print(f"Please enter a valid number between 1 and {max}\n")
            continue
        if num >= 0 and num <= 20:
            print("Great Choice!")
            break
        else:
            print(f"Invalid. Number must be between 1 and {max}")

    # setting the num from input to identify the student from tlgstudent list
    student_name = tlgstudents[num]

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")


    #Bonus 1 - randomly choose a student
    random_num = random.randint(0,20)
    random_student = tlgstudents[random_num]

    #printing random student
    print(f"{random_student}")

if __name__ == "__main__":
    main()









