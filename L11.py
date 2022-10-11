#################################################
#  11.10.2022
#################################################
#  TOPICS TO BE COVERED 
# 👉 CONDITIONAL IN PYTHON
#################################################
################################################
# INDENTATION
################################################


print("Today is Tuesday")
print("Today is good day")
print("Today is Monday")



################################################
# IF..ELIF..ELSE
################################################

# marks = int(input("Enter your total marks: "))
# print("Your marks are : {}".format(marks))

# print(type(marks))


# if marks> 95:
#     print("Grade A")
# if marks> 80:
#     print("Grade B")
# if marks> 75:
#     print("Grade C")

# if marks> 95:
#     print("Grade A")
# # elif marks< 95 and marks >80:
# elif 80 <marks< 95:
#     print("Grade B")
# elif 40 <marks< 80:
#     print("Grade c")
# else:
#     print("Fail")

# we can use n number of elif between if.... else



age_candidate  = int(input("Enter you age: "))


if 0 < age_candidate < 18:
    print("You are not eligible to vote")
elif 18 <= age_candidate < 45:
    print("You are  eligible to vote")
elif 45 <= age_candidate < 60:
    print("You are  eligible to vote")
    print("You  must exercise your rights properly")
elif 60 <= age_candidate < 99:
    print("You are  eligible to vote")
    print("You  can ask office for assistance to vote ")
else:
    print("Enter yor age properly")



################################################
# WHILE LOOP
################################################
# un-countable

#while expression
    # <statement>

i = 1 #initalizing the variable
while i <11: #expression
    print(i) #code to be executed
    i = i + 1 # some point where the expression to be false


