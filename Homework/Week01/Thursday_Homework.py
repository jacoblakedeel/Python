#SMALL ASSIGNMENTS

#ASSIGNMENT 1

# sum = 0
# myList = [2, 4, 6, 8, 10]

# for nums in range(0, len(myList)):
#     sum = sum + myList[nums]

# print(sum)


#ASSIGNMENT 2

# myList2 = [16, 19, 200, 36, 70]

# largest = max(myList2)

# print(f"The largest number is: {largest}")


#ASSIGNMENT 3

# myList3 = [1200, 34, 68, 123, 45]

# smallest = min(myList3)

# print(f"The smallest number is: {smallest}")


#ASSIGNMENT 4


# mylist4 = [17, 34, 56, 33, 89]


# for x in range(5):
#     if (mylist4[x] % 2 == 0):
#         print(mylist4[x])
    

    
#ASSIGNMENT 5

# mylist5 = [-2, 3, 76, -89]

# for pos in range(4):
#     if mylist5[pos] > 0:
#         print(mylist5[pos])




#ASSIGNMENT 6

# mylist6 = [67, -58, 90, -102, 300]
# newlist = []

# for poslist in range(5):
#     if mylist6[poslist] > 0:
#         newlist.append(mylist6[poslist])

# print(newlist)


#ASSIGNMENT 7

# mylist7 = [16, 37, 68, -35, 102]
# factor = 3

# newlist2 = []

# for mult in range(5):
#     newlist2.append(mylist7[mult] * factor)
    
    

# print(newlist2)




#ASSIGNMENT 8


# myString = "Hey there! I'm a string! There's a theory goin around about me."

# print(list(reversed(myString)))





#MEDIUM ASSIGNMENTS

# ASSIGNMENT 1

# nums1 = [2, 68, 10, 12]
# nums2 = [18, 2, 10, 2]

# result_list = [] 

# for mult in range(4): 
#     result_list.append(nums1[mult] * nums2[mult]) 

# print(result_list)


#ASSIGNMENT 2

# Matrix Addition 

# list1 = [[1,3,5,6], [2,4,4,3]]
# list2 = [[5,2,1,0], [1,0,3,5]]
# add_list = []
# for row in range(0, len(list1)):
#     temp = []
#     for column in range(0, len(list1[0])):
#         temp.append(list1[row][column] + list2[row][column])
#     add_list.append(temp)
# print(add_list)


#ASSIGNMENT 3 (Not Complete)


# twoDimList1 = [ [1, 3], [2, 4] ]
# twoDimList2 = [ [5, 2], [1, 0] ]
# result = [ [0, 0], [0, 0] ]
# for outterIndex in range(len(twoDimList1)):
#     for innerIndex in range(len(twoDimList1[outterIndex])):
#         result[outterIndex][innerIndex] = twoDimList1[outterIndex][innerIndex] + twoDimList2[outterIndex][innerIndex]
# print(result)




#ASSIGNMENT 4


# myList = [1,1, 2, 3, 4, 5, 3, 5]
# deDub = []
# for i in range(len(myList)):  # i is the index
#     if myList[i] not in deDub:
#         deDub.append(myList[i])
# #  for item not in myList
# #     deDub.append(item)
# print(deDub)





#ASSIGNMENT 5

# input_string = "I am a leet programmer"
# mapping = {'a': 4,
#            'e': 3,
#            'g': 6,
#            'i': 1,
#            'o': 0,
#            's': 5,
#            't': 7}
# new_string = []
# for character in input_string:
#     if character in mapping:
#         character = str(mapping[character])
#     new_string.append(character)
# new_string = "".join(new_string)
# print(new_string)



#ASSIGNMENT 6

# test_string = input('Enter a word: ')
# vowels = ['a','e','i','o','u']
# new_string = ''
# for i in range(len(test_string)):
#     if i != 0 and test_string[i] == test_string[i-1] and test_string[i].lower() in vowels:
#         new_string += test_string[i] * 3
#     new_string += test_string[i]
# print(new_string)




#ASSIGNMENT 7

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# input_string = "lbh zhfg hayrnea jung lbh unir yrnearq"
# output_string = ""
# for char in input_string:
#     if char != " ":
#         index = alphabet.index(char)
#         new_index = (index + 13) % 26
#         new_char = alphabet[new_index]
#     else:
#         new_char = " "
#     output_string += new_char
# print(output_string)



