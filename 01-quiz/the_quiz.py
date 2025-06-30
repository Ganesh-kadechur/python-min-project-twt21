
print("hello welcome to the world of the quiz the quizzerland")
one = input("do wanna take the simple test on the computer test yes than 1 if not 2 : ")
score = 0
if  one  == "1" :
    print("ok lets try the 5 question  the mini test.")
    # first questions
    ans  =input (f"expand the cpu ").lower()
    if ans == "central processing unit" :
        print("your correct")
        score = 1
    else: 
        print("better luck next time")

    # second question 
    ans  =input (f"what type of data type  8.00 is ").lower()

    if ans == "float":
        print("your correct")
        score = score+1
    else:
        print("better luck next time")
     # third question 
    ans  =input (f"what type of data type  80 is ").lower()

    if ans == "int":
        print("your correct")
        score = score+1
    else:
        print(" better luck next time ")
    # fourth question 
    ans  = input (f"what type of data type  (king) is ").lower()

    if ans == "str":
        print("your correct")
        score = score+1
    else:
        print("better luck next time")

    # fifth  question 
    ans  =input (f"what is python a object oriented language ").lower()

    if ans == "yes":
        print("your correct")
        score = score+1
    else: 
        print("better luck next time")
    
    print("your score is",score)
else:
    print('thanks for the vist')
    
