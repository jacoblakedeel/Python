#ASSIGNMENT 1 - MADLIB FUNCTION


# def input(name, sub):
#     return f"{name}'s favorite subject is {sub}'"

# madlib = input("Jacob", "Literature")

# print (madlib)



#ASSIGNMENT 2 - CELSIUS TO FAHRENHEIT FUNCTION


# def CtoF(c):
#     f = (c * 9/5) + 32
#     return round(f)

# print(CtoF(30))



#ASSIGNMENT 3 - FAHRENHEIT TO CELSIUS FUNCTION


# def FtoC(f):
#     c = (f - 32) * (5/9)
#     return round(c)

# print(FtoC(3))




#ASSIGNMENT 4 - IS EVEN?

# def num(input_num):
#     if input_num % 2 == 0:
#         print(True)
#     else:
#         print(False)

# num(14)




#ASSIGNMENT 5 - IS ODD?

# def num(input_num):
#     if input_num % 2 == 0:
#         print("This number is even")
#     else:
#         print("This number is odd")

# num(15)



#ASSIGNMENT 6 - EVENS ONLY LIST

    
    





#ASSIGNMENT 7 - ODDS ONLY LIST








#  MEDIUM ASSIGNMENTS

# #1. 
# Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.
# It should return the smallest number in the List.


# def small_func(num):
#     result = num[0]
#     for item in num:
#         if item < result:
#             result = item
#     return result

# my_list = [17, 45, 16, 23, 18]
# print(f"The Smallest Number is : {small_func(my_list)}")




#2
# Find the largest number
# Write a function largest that accepts a List of numbers as an argument.

# It should return the largest number in the List.


# def large_func(num):
#     result = num[0]
#     for item in num:
#         if item > result:
#             result = item
#     return result

# my_list = [17, 45, 16, 23, 18]
# print(f"The Largest Number is : {large_func(my_list)}")






#3. Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.


# def short_func(num):
#     result = num[0]
#     for item in num:
#         if  len(result) < len(num):
#             result = item
#     return result


# str_list = ["Hello", "I am long", "I am very long", "I am even longer!"]
# print(f"The shortest string is: {short_func(str_list)}")




# 4. Find the longest String
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.


# def long_func(num):
#     result = num[0]
#     for item in num:
#         if  len(result) > len(num):
#             result = item
#     return result


# str_list = ["Hello", "I am long", "I am very long", "I am even longer!"]
# print(f"The shortest string is: {long_func(str_list)}")




#Large



#1. Tic-tac-toe
# Write a function move that accepts three arguments:

# board a 2-dimensional array that represents a 3x3 tic-tac-toe board
# location a 2-item tuple that specifies an cell on the board
# player a String, either "X" or "Y"
# Return a copy of the board with the player String placed at the location.

# Throw an error if:

# The board is the wrong size
# The location is already occupied by a player
# The location is invalid
# The player String is something other than "X" or "Y"
