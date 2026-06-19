///This is the readme file where I am including all the comments to clarify my approach regarding the code   <br>
///imported the random module to use the random function to generate random numbers   <br>
///Thin created a welcome message for the users   <br>
///After that I defined the losing points as a variable so that it can easily be changed later   <br>
///Then I created a function to use throughout the code for different levels this  helped me reduce redundancy   <br>
Inside the function, I used random function to generate random number to be guessed in the desired range   <br>
Then initialized count to 1   <br>
Used a while loop for continuously asking for users guess unless lost or exited   <br>
Then stored user's guess in a variable   <br>
Then make sure user choose a number in the desired range only   <br>
If user choose a number outside the range then asking user to choose number in the desired range   <br>
Then i created multiple cases: <br>
1>case if user took more than the defined losing points   <br>
    displays the generated number along with a message that the number of tries exceeded the losing point and that the usr lost   <br>
    Used break to get out of the loop if number not guessed correctly and user used all the lives   <br>
2>case if number is guessed correctly   <br>
    displays the number of tries left and tells that it was guessed correctly   <br>
    used break to get out of the loop when user won   <br>
3>case if a higher number is guessed   <br>
    to display number of tries left and give a hint that number is greater than what user guessed   <br>
4>case if a lower number is guessed   <br>
    display number of tries left and give a hint that number is smaller than what user guessed   <br>
then updated count on every valid try   <br>
Now used another while loop continuously gives menu unless exit is chosen   <br>
display the main menu   <br>
took user input of the main menu   <br>
Then defined multiple cases for this menu: <br>
1>case if user wants to exit   <br>
    printed a greeting user after the completion of playing session   <br>
    and used break to close the execution when user choose ot exit   <br>
2>case if user choose to play default level   <br>
    display the level menu   <br>
    display the levels available   <br>
took user input of the level menu   <br>
level-1: 20 numbers   <br>
    if user choose to play level-1   <br>
    call the function for the range 1-20   <br>
level-2: 50 numbers     <br>
    if user choose to play level-2   <br>
    call the function for the range 1-50   <br>
level-3: 100 numbers     <br>
    if user choose to play level-3   <br>
    call the function for the range 1-100   <br>
level-4: 500 numbers   <br>
    if user choose to play level-4   <br>
    call the function for the range 1-500   <br>
level-5: 1000 numbers   <br>
    if user choose to play level-5   <br>
    call the function for the range 1-1000   <br>
custom level:(for any number range)   <br>
3>case if user choose custom level   <br>
    user input for lower limit of the custom range   <br>
    user input for upper limit of the custom range   <br>
    generated a random number in the desired custom range   <br>
    call the function for custom mode   <br>
defined a case if user entered an invalid choice from the menu   <br>
    display a message to input a valid choice   <br>
