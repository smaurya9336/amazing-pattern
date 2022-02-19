#write a program to find Reverse a Number using while loop
from math import remainder
from tokenize import Number


"""Number=int(input("Please Enter any Number:"))
reversed=0
while(Number>0):
    Remainder=Number%10
    reversed=(reversed*10)+Remainder
    Number=Number//10
    print("\n Reverse of entered number is=",reversed)
    """
Number=int(input("Enter any number:"))
RevNum=0
while(Number>0):
    Rem=Number%10
    RevNum=(RevNum*10)+Rem
    Number=Number//10
    print("Reverse Number is:",RevNum)

