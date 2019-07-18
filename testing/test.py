# print("Hello World")
# print("What's up?")
# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")
# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)
# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16
# print(23%4) #3
# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)
# print("Hello" + str(4))
# print(int("4"))

#Inputs!
# firstName= "Harsha"
# lastName= input("What is your last name?\n")
#  print(lastName)
#  print("Nice to meet you "+firstName+" "+lastName.lower().capitalize()+"!")

#  age= int(input("How old are you?\n"))
#  print("You will be "+str(age+3)+" in 2022.")
#  print("You are "+str(age*7)+" in dog years.")
#  if (age >=21): 
#      print("You can legally drink, though you shouldn't")
# if (age+1>=18)
#     print("You can vote in 2020.")










# #Control Flow
# number= input("What's your favorite number?\n")
# try: 
#     num=int(number)
#     if number%2 == 0:
#         print("Your number is even!")
#     else:
#         print("Your number is odd!")
# except:
#     print("Put a number!")





def isGoodTaste(name): 
    favorite= input("What is your favorite food?").capitalize()
    if favorite== "Pizza":
            return "You have a good taste " +name+ "."
    else:
            return "You have a bad taste " +name+ "."
print (isGoodTaste(input("What is your name?")))


