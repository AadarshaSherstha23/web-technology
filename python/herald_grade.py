def grade():
    percentage = int(input("enter your percentage: "))
    if percentage >= 70:
        print("your grade is 'A'")
    elif percentage >= 60 and percentage < 70:
        print ("your grade is 'B")
    elif percentage >= 50 and percentage < 60:
        print("your grade is 'C")
    elif percentage >= 40 and percentage < 50:
        print("Your grade is 'D") 
    else:
        print("you failed")

grade()
    