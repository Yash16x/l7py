print("Select your ride:")
print("1.bike")
print("2.car")

choice= int(input("ENTER YOUR CHOICES:"))
if choice==1:
    print("Which bike:")
    print("1.gpx\n")
    print("2.scooby\n")
    choice2=int(input("Enter you choice:"))
    if choice2==1:
        print("successfuly selected GPX, Cost 20k baht")
    else:
        print("successfuly selected scooby, 10k Baht ")

elif( choice==2):
    print("Which car")
    print("1.BMW")
    print("2.Mclaren")
    choice3=int(input("Enter your choices:"))
    if choice3==1:
        print("successfuly selected BMW, Cost 1mill baht")
    else:
        print("successfuly selected Mclaren, Cost 2mill baht")
