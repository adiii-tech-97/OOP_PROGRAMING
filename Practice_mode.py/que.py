#1). Match Case:

number = input("enter your number:-")
match number:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
    case _:
        print("invalid signal")


#2)Calculator:

choice=int(input("enter your choice:-"))
num = int(input("enter your num:-"))
num1= int(input("enter your num:-"))
match choice:
    case 1:
        print("Addition:-", num + num1)
    case 2:
        print("Substraction:-",num - num1)
    case 3:
        print("muliplication", num * num1)
    case 4:
        print("division", num / num1)
    case _:
        print("invalid operation")


#3)Menu Section:

choice=int(input("enter your choice:-"))
match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Sandwitch")
    case 4:
        print("Pasta")
    case _:
        print("invalid option")


#4)Grade Massage:

Grade=input("enter your marks:-")
match Grade:
    case "A":
        print("Exallent")
    case "B":
        print("Verry Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")


#5)Traffic signal:

colour= input("Enter your colour" )
match colour:
    case "red":
        print("Stop")
    case "Yellow":
        print("Ready")
    case "Green":
        print("Go")
    case _:
        print("invalid signal")


#6)Number Category:

choice = int(input("enter your choice"))
match choice:
    case "1":
        print("Hii")
    case "2":
        print("Good Morning")
    case "3":
        print("What is your name")
    case "4":
        print("How are you")
    case "5":
        print("Thank you")
    case _:
        print("Byyyyyy")

#7)Month name:

choice = int(input("enter your choice"))
match choice:
    case "1":
        print("January")
    case "2":
        print("February")
    case "3":
        print("March")
    case "4":
        print("April")
    case "5":
        print("may")
    case "6":
        print("june")
    case "7":
        print("july")
    case "8":
        print("August")
    case "9":
        print("September")
    case "10":
        print("October")
    case "11":
        print("November")
    case "12":
        print("December")
    case _:
        print("invalid match")


#8)user category:

choice=input("enter your choice")
match choice:
    case "Umesh" |"Rajesh"| "Mukes":
        print("Group-1")
    case "Chetan"|"Shubham"| "Akash":
        print("Group-2")
    case _:
        print("unknown candidate")


#9)Simple ATM Menu:

balance=int(input("Enter your balance:-"))
while True:
    print("1.Check Balance.")
    print("2.Deposite Money")
    print("3.Withdraw Money")
    print("4.Exit")
    choise=input("Enter you are choise:-")
    match choise:
        case "1":
            print("You are balance:-",balance)
        case "2":
            v=int(input("Enter a amount:-"))
            balance+=v
            print("Desposite sucessfully",balance)
        case "3":
            g=int(input("Enter withdrawl  amount:-"))
            if g>balance:
                print("Invalid balance.")
            else:
                balance-=g
                print("withdrawl sucessfully.")
                print("Remaning balance",balance)
        case "4":
            print("Exiting programming.......")
            break
        case _:
            print("Invalid choise,please try again")

#10)Vehicle Type:

choice=input("enter your choice")
match choice:
    case "Four or more wheele":
        print("Car / Bus / Truck")
    case "Two wheeler":
        print("Bike / Scooter")
    case "Cycle":
        print("Bicycle")
    case _:
        print("unknown vehicle")

