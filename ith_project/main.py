# # DAY 02 Lecture
#
# values = [1,2,3]
# values.append(4)
# values.remove(1)
# print(values)
#
# # Example 2
#
# values2 = (1, 2, 3)
# print(type(values2))
#
# # Example 3
#
# values3 = {1, 2, 3, 4, 3, 3, 5, 6}
# print(values3)
# print(type(values3))
#
# # Example 4
#
# values4 = {
#     "name": "pele",
#     "age": 20,
#     "email": "pele@gmail.com"
#
# }
#
# # Test 1
#
# number = input("Type a number: ")
# result = 0
# i = 0
# while i< int(number):
#     i = i+1
#     result += i
#
#
# print(result)
#
# # Test 2
#
# textlist = ["Hej", "på", "dig", "hur", "mår","du", "?"]
#
# mytext = ""
#
# for i in textlist:
#
#     mytext += i + " "
#
#
# print(mytext)
#
# # Function def use kore function likha
#
# # example 1 function
# def myfunction(name:str):
#     print("hello ", name)
#
# myfunction("Holy")
#
# # example 2 function
#
# def myfunction2(name: str, age: int):
#     print("Hello ", name, "You are ", age, " years old!")
#
# myfunction2("Holy", 37)
#
# # example 3 function
#
# def myfunction3(a = 10, b = 20, c = 20, d = 7):
#     print(a, b, c, d)
#
# myfunction3(10, 40, 0, 20)
#
# # Keyword Args
# # Tupple
# min_lista = [1,2,3,4,5]
# min_lista[2] = 20
# min_lista.append(6)
# min_lista.remove(4)
# print(min_lista)
#
# min_tupple = ('a','b','c')
#
#
# #  function again
#
# # def func(value):
# #     return value*2
# #
# # return_value = func(10)
# # print(return_value)
#
# def func(value):
#     return value, value*2, value*3
#
# a,b,c = func(10)
# print(a,b,c)
#
# #-------
# def func(value):
#     return value, value * 2, value * 3, value * 4
#
#  func(10)


 # Uppdrag 3
# for i in [1,2,3, 'anna', True]:
#     print(i)
#
# for i in [1,2,3, 'anna', True]:
#     print('Hej', i)


# 10 theke shuru hobe numbering
# for i, value in enumerate(['Holy','Farabi','Fariha','Nahir'],10):
#     print(i, value)

# value = list(range(2,100,4))
# print(value)

# id-statement

# x=10
# y=20
# if x>10:
#     print('Bigger than 10')
# else:
#     print('Less or equal to 10')


# Day 04

# LAB 01
def magical_stairs():

    for step in range(21):
        if step % 3 == 0:
            print('Ett magiskt hinder här!')
        else:
            print(f'Kliver på trappsteg {step} och finner en gnistrande magi!')

print('Välkomna till den Magiska Trappan!')
magical_stairs()


# LAB 02
def mystical_show(magic_list):
    i = 1
    for magic in magic_list:
        print(f'Magi #{i}: {magic}')
        i+=1

magic_list = ['Svävande hatt', 'Magisk fågel', 'rullande boll', 'försvunnet kort']
mystical_show(magic_list)

# LAB03

def add_student(student_list, namn, betyg):
    if not student_list:
        print('Det finns ingen elev i listan')

    for student in student_list:
        if student['namn'] == namn:
            student['betyg'] = betyg
            print('Dictionary Updated')

    return {'namn': namn, 'betyg': betyg}



def show_students(student_list):
    for student in student_list:
        print(f"Student Name: {student['namn']} and Betyg: {student['betyg']} \n")


def get_top_student(student_list):
    for student in student_list:
        if student['betyg'] == 'A':
            print(f"Top student's Name: {student['namn']} and Betyg: {student['betyg']} \n")

should_continue = True
student_list = []
while should_continue:
    namn = input('Vad är din namn? ')
    betyg = input('Vad är din betyg? ')

    student_list.append(add_student(student_list, namn, betyg))
    users_choice = input('vill du fortsätta? Yes/ No :')
    if users_choice == 'No':
        should_continue = False






show_students(student_list)
get_top_student(student_list)
