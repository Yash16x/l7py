med=input("Do you have medical cause for absentees:")
att=int(input("Enter your attendence in number:"))
if med=="yes" or med=="Yes" or med== "YES":
    print("You are allowed to take the exam")
else:
    if att>=75:
        print("You are allowed to take the exam")
    else:
        print("You are not allowed to take the exam")
