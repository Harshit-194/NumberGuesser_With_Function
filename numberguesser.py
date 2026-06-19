import random #importing thr random module to generate random numbers
print("Welcome to the Number Guesser")#welcome message for the users
lose_point=5#defined the losing points
def else_part_of_inner_loop(lower, upper):#created a function to use throughout the code for different levels
    system_number = random.randint(lower, upper)#generate random number to be guessed in the desired range
    count = 1#initialized count to 1
    while True:#keeps asking for users guess unless lost or exited
        user_number = int(input(f"Choose a number {lower} to {upper}: "))#taking user's guess as input
        if upper < user_number or user_number < lower:#to make sure user choose a number in the desired range
            print(f"please choose a number between {lower} and {upper}")#asking user to choose number in the desired range only if chosen outside the range
        else:
            if count == lose_point:#case if user took more than the defined losing points
                print(f"Your tries exceeded {lose_point}, the number was {system_number}, you lost!!!!!!!!!!")#displays the generated number along with a message that the number of tries exceeded the losing point and that the usr lost
                break#to get out of the loop if number not guessed correctly and user used all the lives
            else:
                if user_number == system_number:#case if number is guessed correctly
                    print(f"You correctly guessed the number {user_number} with {lose_point - count} tries left!!")#displays the number of tries left and tells that it was guessed correctly
                    break#to get out of the loop when user won
                elif user_number < system_number:#case if a higher number is guessed
                    print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")#to display number of tries left and give a hint that number is greater than what user guessed
                elif user_number > system_number:#case if a lower number is guessed
                    print(f"Incorrect!!! {lose_point - count} tries left !!!!!!S Try a lower number!!!!")#to display number of tries left and give a hint that number is smaller than what user guessed
            count = count + 1#to update count on every valid try

while True:#continuously gives menu unless exit is chosen
    print("--------------------Main Menu---------------------\n1>Default Game(number start from 1)\n2>User defined Game\n3>quit")#to display the main menu
    choice1 = int(input("enter your choice number from menu:"))#to take user input of the main menu
    if choice1==3:#case if user wants to exit
        print("THANK YOU for playing!!!")#greeting user after the completion of playing session
        break#to close the execution when user choose ot exit
    elif choice1==1:#case if user choose to play default level
        print("You have entered default game zone:\n---------------------Menu for levels---------------------")#to display the level menu
        print("1. very easy(20 numbers)\n2. easy(50 numbers)\n3. medium(100 numbers)\n4. hard(500 numbers)\n5. Expert(1000 numbers)")#to display the levels available
        choice2=int(input("enter your choice number from menu:"))#to take user input of the level menu




        # level 1: 20 numbers
        if choice2==1:#if user choose to play level-1
            else_part_of_inner_loop(1,20)#calling the function for the range 1-20

        elif choice2==2:#if user choose to play level-2
            else_part_of_inner_loop(1,50)#calling the function for the range 1-50

        elif choice2==3:#if user choose to play level-3
            else_part_of_inner_loop(1,100)#calling the function for the range 1-100

        # level 4: 500 numbers
        elif choice2==4:#if user choose to play level-4
            else_part_of_inner_loop(1,500)#calling the function for the range 1-500


        #level 5: 1000 numbers
        elif choice2==5:#if user choose to play level-5
            else_part_of_inner_loop(1,1000)#calling the function for the range 1-1000


    #custom level:
    elif choice1==2:#case if user choose custom level
        lower2=int(input("enter lower number: "))#lower limit of the custom range
        upper2=int(input("enter upper number: "))#upper limit of the custom range
        System_number2=random.randint(lower2, upper2)#generating a random number in the desired custom range
        else_part_of_inner_loop(lower2,upper2) #calling the function for custom mode
    else:#case if user entered an invalid choice from the menu
        print("please enter a valid input!!!")#display a message to input a valid choice
