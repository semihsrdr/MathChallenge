import random
import time

#Math Challenge
#This project uses functions, try catch

def createQuestion():
    operations=["*","-","+","/"]
    first_number=random.randint(1,15)
    second_number=random.randint(1,15)
    chosed_operation=operations[random.randint(0,3)]

    if chosed_operation=="*":
        print(first_number, chosed_operation, second_number)
        return first_number*second_number
    elif chosed_operation=="-":
        print(first_number, chosed_operation, second_number)
        return first_number-second_number
    elif chosed_operation=="+":
        print(first_number, chosed_operation, second_number)
        return first_number+second_number
    else:
        while first_number%second_number!=0:
            first_number = random.randint(1, 15)
            second_number = random.randint(1, 15)
        print(first_number, chosed_operation, second_number)
        return first_number/second_number

question_counter=0
true_answers=0

print("Welcome to the Math Challenge!")
while True:
    answer=input("Do you wanna start (yes,no) : ")
    if answer.lower()=="yes":
        while question_counter<11:
            solution=createQuestion()
            question_counter += 1
            try:
                player_answer=int(input(""))
                if player_answer==solution:
                    true_answers+=1
            except ValueError:
                print("please enter the number")


        print("Number of true answers :",true_answers)
        print("Number of false answers :",11-true_answers)
        print("-----------------------------------------------------------------------------------------------------")
    elif answer.lower()=="no":
        print("The Game is shutting down...")
        time.sleep(1)
        print("The game shutted down!")
        break