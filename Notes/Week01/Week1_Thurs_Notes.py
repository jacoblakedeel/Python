# #Thursday Notes

# day1 = "Sunday"
# day2 = "Monday"
# day3 = "Tuesday"
# day4 = "Wednesday"
# day5 = "Thursday"
# day6 = "Friday"
# day7 = "Saturday"

# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#----------0---------1----------2----------3------------4----------5----------6

# days[0]
# print(days[0])

#len() prints length of list

# days [5] = "FRYday" ----changes Friday to FRYday

# print(days)

# numsArray = [1, 2, "Hey", 6.2,]
# print(numsArray)

# numsArray[2] = "Hello"

# numsArray.append(99)
# print(numsArray)



# numsArray = [1, 2, "Hey", 6.2,]

# count = 0

# print(len(numsArray))

# while (count < len(numsArray)):
#     print(f"{count}: {numsArray[count]}")
#     count += 1


# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]         #could also us append()
# c = a + b
# print(c)


# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# additionalTodos = ["binge watch a show", "go to sleep"]

# result = todos.append(additionalTodos)  #--------technically puts a list inside a list
# print(todos)


# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# additionalTodos = ["binge watch a show", "go to sleep"]

# result = todos.extend(additionalTodos)  

# # del todos[0]
# print(todos)

# num = [4, 6, 7, 8, 9]

# del num[0:2]

# print(num)

# nums = [4, 6, 7, 8, 9]

# subList = nums[1:4]    #-----------slice creates new list [6, 7, 8]

# print(subList)



# nums = [4, 6, 7, 8, 9]

# nums.insert(3, 101)  #----------inserted 101 into index 3

# print(nums)


# nums = [4, 6, 7, 8, 9]

# print(nums)

# popped_nums = nums.pop()  #----------popped off last element from list

# print(popped_nums)

# print(nums)



# nums = [4, 6, 7, "eight", 9]

# result = nums.index("eight")   #----------must enter what you are looking for. will print the index

# print(result)




# matrix = [[0, 1], [2, 3]]

# print(matrix[0][0])  #---------prints 0



# a = [ [2, 4, 6, 8 ],  
#     [ 1, 3, 5, 7 ],  
#     [ 8, 6, 4, 2 ],  
#     [ 7, 5, 3, 1 ] ] 

# outerIndex = 0
# innerArrIndex = 0

# while outerIndex < len(a):
#     print(a[outerIndex])
#     while innerArrIndex < len(a[outerIndex]):
#         print(a[outerIndex][innerArrIndex])
#         innerArrIndex += 1
    
#     innerArrIndex = 0
#     outerIndex += 1



#strings as lists

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# # index = 0
# # while index < len(alphabet):
# #     print(alphabet[index])
# #     index += 1

# alphList = list(alphabet)
# alphJoin = " ".join(alphList)

# print(alphabet)
# print(alphList)
# print(alphJoin)




# num = 1
# multi = 1

# while num < 11:
#     print(num "")




# constants = (3.14, 2.72)   #---------Tuple. Can not be changed.

# print(constants[0])



# result = list(range(10, 20, 2))
# print(result)


#FOR LOOPS

# names = ["Claude", "Ian", "Zach", "Matthew", "Kim", "Susan"]

# for nameElement in names:
#     print(nameElement)


# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for letter in alphabet:
#     print(letter)

# for num in range(0, 6):
#     print(num)


# for outer in range(1, 11):
#     for inner in range(1, 11)
#     print(f"{outer} x {inner} = {outer * inner}")