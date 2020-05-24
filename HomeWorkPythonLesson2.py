# 6. Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.
total_6 = 0
index_6 = 0
while index_6 < 5:
    number_6 = int(input("tell me any number "))
    question_6 = input("do you want to add it? " )
    if question_6.casefold() == "yes":
        total_6 += number_6
        index_6 += 1
    else:
        index_6 +=1
print(total_6)

# 7. Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.
direction = input("Tell me, which direction you want to count? Up or Down? ")
if direction.casefold() == "up" :
    number_7 = int(input("Tell me the top number "))
    for i in range(1,number_7 + 1):
       print(i)

elif direction.casefold() == "down" :
    number_7_2 = int(input("Tell me any number below 20 "))
    for i_2 in range(20, number_7_2 - 1, -1):
        print(i_2)
else:
    print("I don't understand! ")

# 8. Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.
quantity_8 = int(input("How many people are invited? "))

if quantity_8 < 10 :
    index = 0
    while index < quantity_8 :
        name_8 = input("Tell me the name? ")
        print(f'{name_8} hase been invited')
        index += 1
else:
    print("Too many people")

# 9. Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and print the message “The total is… [total]”. Stop the loop when the total is over 50.
total_9 = 0
while total_9 <= 50:
    number_9 = int(input("Tell me any number? "))
    total_9 += number_9
    print(f'The total number is {total_9}')

# 10. Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program.
number_10 = int(input("Enter a number "))
while number_10 < 5 :
    number_10 = int(input("Enter a number "))
    if number_10 >= 5:
        print(f'The last number you entered {number_10}')
        break

# 11. Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.
number_11 = int(input("Tell me any number. "))
number_11_2 = int(input("Tell me another number. "))
result_11 = number_11 + number_11_2
question_11 = input("Do you want to add another number? ")
while question_11.casefold() == "y" :
    string_11 = input("tell me another number? ")
    result_11 += int(string_11)
    question_11 = input("Do you want to add another number? ")
print(f'Total is {result_11}')

# 12. Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.
name_12 = input("Tell me the name, you want to invite to the party? ")
count_12 = 0
print(f'{name_12} has now been invited to the party')
count_12 += 1
name_12_2 = input("Do you want to invite someone else? ")
while name_12_2.casefold() == 'yes' :
    name_12_3 = input("Tell me his/her name? ")
    print(f'{name_12_3} has now been invited to the party')
    count_12 += 1
    name_12_2 = input("Do you want to invite someone else? ")
print(count_12)

# 13. Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.
number_13 = int(input("Tell me the number between 10 and 20 "))

while number_13 not in range(10,21) :
    if number_13 < 10 :
        print("Too low")
        number_13 = int(input("Tell me the number between 10 and 20 "))
    elif number_13 > 20 :
        print("Too high")
        number_13 = int(input("Tell me the number between 10 and 20 "))
print("Thank you")

# 15. Write a Python program to multiplies all the items in a list.
list_15 = [1,5,6,8,-2]
result_15 = 1
for item_15 in list_15:
    result_15 *= int(item_15)
print(result_15)

# 17. Write a Python program to get the smallest number from a list

list_16 = [ 1 ,2 ,4 , -99, 101 , -101, -1, 98]
print(min(list_16))
#OR
min_16 = list_16[0]
for item_16 in list_16 :
    if item_16 < min_16:
        min_16 = item_16
print(min_16)

# 18. Write a Python program to remove duplicates from a list.
list_18 = [2 , 4, 8, 2, 9, 3, 9, 4, 2, 7]
result_18 = list()
for item_18 in list_18:
    if item_18 not in result_18:
        result_18.append(item_18)
print(result_18)

# 19. Write a Python program to check a list is empty or not.
list_19 = [1, 3, 8, 9, 4, 7, 5]
print(len(list_19) >= 1)

# 20. Write a Python function that takes two lists and returns True if they have at least one common member.
list_20_1 = [ 1, 4, 5, 7, 8, 9, 12]
list_20_2 = [ 2, 3, 6, ]
result_20_1 = False
for item_20 in list_20_1:
    if item_20 in list_20_2:
        result_20_1 =True
print(result_20_1)
#OR
# result_20 = False
# for item_1 in list_20_1:
#     for item_2 in list_20_2:
#         if item_1 == item_2:
#             result_20 = True
# print(result_20)

# 21. Write a Python program to get unique values from a list.
list_21 = [1, 3, 5, 7, 10, 5, 3,11, 12]
result_21 = []
for item_21 in list_21:
    if item_21 not in result_21:
        result_21.append(item_21)
print(result_21)

# 22. Write a Python program to select the odd items of a list.

list_22 = [2, 3, 5, 6, 9, 8, 12, 24, 33, 35]
result_22 = []
for item_22 in list_22:
    if item_22 % 2 == 0:
        result_22.append(item_22)
print(result_22)

# 23. Write a Python program to concatenate elements of a list
list_23 = ['Hello', 'world',  "all", ]
string_23 = ''.join(list_23)
print(string_23)
#OR
list_24 = [1, 3, 5, 7]
result_24 = ''
for item_24 in list_24:
    result_24 += str(item_24)
print(result_24)
#OR
list_25 = ['Hello', 1, True]
result_25 = ''
for item_25 in list_25:
    result_25 += str(item_25)
print(result_25)















