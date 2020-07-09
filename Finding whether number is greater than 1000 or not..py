#Finding whether a number is greater than 1000 or not.

Num1=int(input("Please enter your number : "))

#Writing code to verify.

if Num1 > 1000:
    print("Your number is greater than 1000")
    Difference=Num1-1000
    print("The difference between your no. and 1000 is: " + str(Difference))
    
else:
    print("Your number is not greater than 1000")