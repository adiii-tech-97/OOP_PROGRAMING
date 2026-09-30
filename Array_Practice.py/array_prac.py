

#1)
class odd_numbers:
    try:
        def __init__(self):
            pass
        def num(self):
            for i in range(1,51):
                if i%5 == 0:
                    continue
                elif i%2 != 0:
                    print(i)
    except ValueError:
        print("invalid value please enter the valid value")

c1 = odd_numbers()
c1.num()


print("------------------------------")

#2)
class numbers:
    try:
        def __init__(self):
            pass
        def num(self):
            for i in range(1,101):
                if i%7 == 0 and i%9 == 0:
                    break
                print(i)
    except TypeError:
        print("enter the valid data type")

obj = numbers()
obj.num()


print("--------------------------")

#3)
class reverse_num:
    try:
        def __init__(self):
            pass
        def num(self):
            i=10
            while i>=1:
                if i == 6:
                    i-=1
                    continue
                print(i)
                i-=1
    except ValueError:
        print("enter the valid value")

obj = reverse_num()
obj.num()



print("--------------------------")

#4)
class emp_names:
    try:
        def __init__(self):
            pass
        def name(self):
            names = ["mahesh","rakshak","akash","admin","ram"]
            for i in names:
                if i == "admin":
                    break
                print(i)
    except TypeError:
        print("wrong data type")

p1 = emp_names()
p1.name()



print("--------------------------")

#5)
class even_num:
    try:
        def __init__(self):
            pass
        def operation(self):
            i=1
            while i<=10:
                if i%2 == 0:
                    print(i)
                i+=1
    except TypeError:
        print("wrong data type")

obj1 = even_num()
obj1.operation()

 
print("--------------------------")       

#6)
class charactor:
    try:
        def __init__(self):
            pass
        def words(self):
            line = "Just looking like a wow"
            for i in line:
                if i.lower() not in "aeiou":
                    print(i)
    except TypeError:
        print("this data type is wrong")

obj = charactor()
obj.words()


print("--------------------------")   

#7)
class check_num:
    try:
        def __init__(self):
            pass
        def numbers(self):
            n=int(input("enter the number"))
            num = [10,20,30,40,50,60,70,80,90,100]
            for i in num:
                if i==n:
                    print("number is existed")
                    break
                else:
                    print("number is not exited")
                    break
    except ValueError:
        print("please enter the valid number")

n1 =check_num()
n1.numbers()



print("--------------------------")   

#8)
class intergers:
    try:
        def __init__(self):
            pass
        def num(self):
            for i in range(1,21):
                if i == 13:
                    continue
                print(i)
    except ValueError:
        print("invalid value")

b1 = intergers()
b1.num()



print("--------------------------")   

#9)
class even_num:
    try:
        def __init__(self):
            pass
        def numbers(self):
            for  i in range(1,11):
                if i%2 == 0:
                    pass
                else:
                    print(i)
    except ValueError:
        print("invalid value")

p1 = even_num()
p1.numbers()



print("--------------------------")   

#10)
class values:
    try:
        def __init__(self):
            pass
        def num(self):
            count=0
            for i in range(1,101):
                m1= i%3 == 0
                count+=m1
            print(count)
    except TypeError:
        print("wrong data type")

c1 = values()
c1.num()



print("--------------------------")   


#11)


