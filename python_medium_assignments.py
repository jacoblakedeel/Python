#ASSIGNMENT 1: TIP CALCULATOR

# bill_amount = float(input("How much was the bill? "))
# service_grade = input("How was the service? Good, Fair, or Bad? ").strip().lower()

# if service_grade == "good":
#     tip_amount = .20
# elif service_grade == "fair":
#     tip_amount = .15
# elif service_grade == "bad":
#     tip_amount = .10
# else:
#     print("Please describe your service.")

# print(f"Tip amount: {tip_amount}")

# total_bill = bill_amount + tip_amount

# print(f"Total Bill: {total_bill}")



#ASSIGNMENT 2: SPLIT CHECKS

# bill_amount = float(input("How much was the bill? "))
# service_grade = input("How was the service? Good, Fair, or Bad? ").strip().lower()
# split_ways = int(input("How many ways would you like to split the check? "))

# if service_grade == "good":
#     tip_amount = .20
# elif service_grade == "fair":
#     tip_amount = .15
# elif service_grade == "bad":
#     tip_amount = .10
# else:
#     print("Please describe your service.")

# print(f"Tip amount: {tip_amount}")

# total_bill = bill_amount + tip_amount
# amount_per_person = total_bill/split_ways

# print(f"Total Bill: {total_bill} \nAmount per person: {amount_per_person}")




#ASSIGNMENT 3: COINS

# user_coins = 0
# user_answer = (input("Would you another coin? "))

# while user_answer == "yes".lower():
#     user_coins += 1
#     print(f"Your coin total is now: {user_coins} coins")
#     user_answer = input("Another? ")
# else:
#     print("Complete")    




#ASSIGNMENT 4: BUILD A BOX (ALMOST)

# print("Time to build a box!")

# height = int(input("How high would you like your box? "))
# width = int(input("How wide would you like your box? "))

# top = ("* " * width)
# side = ("\b*\n " * height)
# second_side = (width * " *")
# bottom = ("* " * width)
# print(top, side, bottom, second_side)




#ASSIGNMENT 5: TRIANGLE

#I do not understand this problem. Found this solution online.

# print("Now let's build a triangle!")

# n = 0
# r = 6
# for m in range(1, r+1):
#     for gap in range(1, (r-m)+1):
#         print(end="  ")
#     while n != (2*m-1):
#         print("* ", end="")
#         n += 1
#     n = 0
#     print()



#ASSIGNMENT 6: MULTIPLICATION TABLE

# num = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5
# num6 = 6
# num7 = 7
# num8 = 8
# num9 = 9
# num10 = 10

# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)
# for i in range(1, 11):
#    print(num2, 'x', i, '=', num2*i)
# for i in range(1, 11):
#    print(num3, 'x', i, '=', num3*i)
# for i in range(1, 11):
#    print(num4, 'x', i, '=', num4*i)
# for i in range(1, 11):
#    print(num5, 'x', i, '=', num5*i)
# for i in range(1, 11):
#    print(num6, 'x', i, '=', num6*i)
# for i in range(1, 11):
#    print(num7, 'x', i, '=', num7*i)
# for i in range(1, 11):
#    print(num8, 'x', i, '=', num8*i)
# for i in range(1, 11):
#    print(num9, 'x', i, '=', num9*i)
# for i in range(1, 11):
#    print(num10, 'x', i, '=', num10*i)
