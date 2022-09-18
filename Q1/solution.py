## Add code below with answer clearly stated
# Q1: Finding the Sum of Numbers in 100!

"""
The function will recieve a number input by the user. After that it will calculate its factorial and store it in the Factorial
variable. After that we will convert the factorial into a string of digits with the help to typecasting str(int) function
and store it in factorialString variable. We will then traverse through the said string of digits (factorialString) and pick up
each character one by one and convert it back to its original interger form by typecasting int("str") function and add it
to our variable sumOfFactorial, which was initialized by 0 previously.  sumOfFactorial will contain our final result and it
will be returned upon function completion.
"""


def sumOfFactDigits(inputNumber):
    Factorial = 1;  # Declaring our

    for i in range(1, inputNumber + 1):
        Factorial = Factorial * i;

    factorialString = str(Factorial);
    sumOfFactorial = 0;

    # In this for
    for i in factorialString:
        sumOfFactorial = sumOfFactorial + int(i);

    return sumOfFactorial;


"""
Here we ask the user to give us a number to play with. That num is stored in variable Number. Variable Number is then passed 
into our function sumOfFactDigits(). It returns our result which is stored in variable Answer.
"""
Number = int(input("Please enter your desired Number: "));
Answer = sumOfFactDigits(Number);
print("Your Answer is:", Answer);


