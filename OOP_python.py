

#1) Print all numbers from 1 to 10 using a loop.


class number:
    def num():
        for i in range(1,11):
            print(i)
number.num()


#2) Print numbers from 10 down to 1 in reverse order.

class number:
    def num():
        for i in range(11,0,-1):
            print(i)
number.num()


#3) Print all even numbers between 1 and 100.


class data:
    def num():
        for i in range(1,101):
            if i%2 == 0:
                print(i)
data.num()


#4) Print all odd numbers between 1 and 100.


class data:
    def __init__(self):
        print("Constructor called")
    def num(self):
         for i in range(1,10):
              if i%2 != 0:
                print(i)
s1=data()
s1.num()


#5) Print the multiplication table of a given number from n × 1 to n × 10.


class mul_table:
    def __init__(self):
        print("multiplication table")
    def table(self):
        for i in range(1,11):
            v=i*n
            print(v)
n=int(input("enter youe number"))
data=mul_table()
data.table()


#6) Calculate and print the sum of the first n natural numbers.


class addition:
    def __init__(self,n):
        self.n = n
    def data(self):
        sum = 0
        for i in range(1,n+1):
            sum += i
        print(sum)
n=int(input("enter a number:"))
tot=addition(n)
tot.data()

#7) Calculate the sum of all even numbers from 1 up to n.

class even_no:
    def __init__(self,n):
        self.n = n
    def data(self):
        sum = 0
        for i in range(1,n+1):
            if i%2 == 0:
                sum += i
        print(sum)
n=int(input("enter your number:"))
obj=even_no(n)
obj.data()


#8) Calculate the sum of all odd numbers from 1 up to n.

class odd_no:
    def __init__(self,n):
        self.n = n
    def data(self):
        sum = 0
        for i in range(1,n+1):
            if i%2 != 0:
                sum += i
        print(sum)
n=int(input("enter your number:"))
total=odd_no(n)
total.data()


#9) Calculate and print the factorial of a given number.

class factorial:
    def __init__(self,n):
        self.n = n
    def fact(self):
        fact_no = 1
        for i in range(1,n+1):
            fact_no = fact_no*i
        print(fact_no)
n=int(input("enter your number:"))
no=factorial(n)
no.fact()

#10) Find and print the product of all digits of a given number.

class product:
    def __init__(self,n):
        self.n = n
    def data(self):
        pro = 1
        while n > 0:
            pro*= n%10
            n=n//10
        print(pro)
n=int(input("enter your number:"))
p1=product(n)
p1.data()


#11)
class data():   
    def __init__(self,n):
        self.n = n
    def tot(self):
        count = 0
        while self.n > 0:
            self.n=self.n//10
            count+=1
        print(count)
n=int(input("enter your number:"))
t1=data(n)
t1.tot() 


#12)
class data:
    def __init__(self,n):
        self.n = n
    def number(self):
        n=self.n
        rev = 0
        while n>0:
            digit=n%10
            rev=rev*10+digit
            n=n//10
        print(rev)
n=int(input("enter tour number:"))
n1 = data(n)
n1.number()


#13)
class data:
    def __init__(self,n):
        self.n = n
    def value(self):
        n=self.n
        rev = 0
        original=n
        while n > 0:
            digit = n%10
            rev = rev*10 + digit
            n = n//10
        print(rev)
        if original == rev:
            print("palindrom")
        else:
            print("not palindrom")
n=int(input("enter your number:"))
p1 = data(n)
p1.value()

#14)
class number:
    def __init__(self,n):
        self.n = n
    def data(self):
        n=self.n
        sum = 0
        while n > 0:
            sum+=n%10
            n=n//10
        print(sum)
n=int(input("enter your number:"))
d1=number(n)
d1.data()


#15)
class number:
    def __init__(self,n):
        self.n = n
    def num(self):
        n= self.n
        check=0
        og = n
        while n >0:
            digit=n%10
            check+=digit**3
            n=n//10
        if og==check:
            print("armstrong number:")
        else:
            print("not armstrong number:")
n=int(input("enter your number:"))
A1=number(n)
A1.num()


#16)
class perfect:
    def __init__(self,n):
        self.n = n
    def data(self):
        n=self.n
        for i in range(2,n+1):
            sum=0
            for j in range(1,i):
                if i%j == 0:
                    sum += j
            if sum == i:
                print(i)
n=int(input("enter your number:"))
p1 = perfect(n)
p1.data()


#17)
class number:
    def __init__(self,num):
        self.num = num
    def prime(self):
        for i in range(1,101):
            if i==2:
                print("prime number:",i)
            elif i == 3:
                print("prime number:",i)
            elif i%2 == 0 or i%3 == 0:
                print("not a prime number:",i)
            else:
                print("prime number:",i)
n1=number(100)
n1.prime()

#18)
class numbers:
    def __init__(self,n):
        self.n = n
    def data(self):
        if n == 2:
            print("prime number:",n)
        elif n == 3:
            print("prime number:",n)
        elif n%2 == 0 or n%3 == 0:
            print("not a prime number:",n)
        else:
            print("prime number:",n)
n=int(input("enter your number:-"))
d1=numbers(n)
d1.data()


#19)
class Fibonacci:
    def __init__(self,n):
        self.n = n
    def data(self):
        a=0
        b=1
        print("0 1",end=" ")
        c=a+b
        for i in range(1,self.n):
            if c<=self.n:
                print(c,end=" ")
                a=b
                b=c
                c=a+b
n=int(input("enter yur number:"))
c1 = Fibonacci(n)
c1.data()

#20)
class fibonacci_num:
    def __init__(self,n):
        self.n = n
    def data(self):
        sum = 0
        a = 0
        b = 1
        print("0 1",end=" ")
        c = a+b
        sum = 1
        for i in range(1,n):
            if c<=n:
                c=a+b
                print(c,end=" ")
                a=b
                b=c
                sum+=c
        print("\n",sum)
n=int(input("emter your number:-"))
d1=fibonacci_num(n)
d1.data()


#1)

print("1).\n-------------------------")

class vehicle:
    def __init__(self):
        pass
    def start(self):
        print("vehicle is start")
class car(vehicle):
    def drive(self):
        print("car is driving")
car1=car()
car1.start()
car1.drive()


print("2).\n-----------------------")

#2)
class person:
    def __init__(self,name = "adi",age = 21):
        self.name =name
        self.age =age 

class student(person):
    def __init__(self,roll_no):
        self.roll_no =roll_no
        person.__init__(self)
p1 =student(11)
print(p1.roll_no)
print(p1.name)
print(p1.age)


print("3).\n------------------------")


#3)
class employee:
    def __init__(self,name = "adi",salary = 12345):
        self.name=name
        self.salary=salary
class devloper(employee):
    def __init__(self):
        employee.__init__(self)
obj = devloper()
print(obj.name)
print(obj.salary)

print("4).\n-----------------------")

#4)
class employee:
    def login(self):
        print("employee logged in:")
    def logout(self):
        print("employee logged out")
class devoper(employee):
    def writecode(self):
        print("writing code :")
p1= devoper()
p1.login()
p1.logout()
p1.writecode()


print("5)\n.----------------------")


#5)
class father:
    def __init__(self):
        pass
    def  father_property(self):
        print("bike")
class mother:
    def __init__(self):
        pass
    def mother_property(self):
        print("car")
class son(father,mother):
    def __init__(self):
        pass
    def son_activity(self):
        print("learning")
p1 = son()
p1.son_activity()
p1.father_property()
p1.mother_property()

print("6).\n-------------------------")


#6)
class person:
    def show_name(self):
        print("Adi")
class employee(person):
    def show_salary(self):
        print("45000")
class manager(employee):
    def deparment(self):
        print("developer")
o1 = manager()
o1.show_name()
o1.show_salary()
o1.deparment()

print("7).\n-----------------------")

#7)
class employee:
    def login(self):
        print("eployee logged in")
class developer(employee):
    def write_code(self):
        print("work on project")
class tester(employee):
    def test_software(self):
        print("software is done")

obj1 = developer()
obj1.login()
obj1.write_code()

print("::~~~~~~~~~~~~~~~~::")

obj2 = tester()
obj2.login()
obj2.test_software()

print("8).\n-------------------------")

#8)
class animal:
    def Eat(self):
        print("Eating a food")
class Dog(animal):
    def Bark(self):
        print("Bhoo,Bhoo") 
class Cat(animal):
    def Meow(self):
        print("Meow,Meow")
class Puppy(Dog,Cat):
    def Play(self):
        print("play as a friend")
p1 = Puppy()
p1.Eat()
p1.Bark()
p1.Meow()
p1.Play()


print("------------------------")


print("1)=================================")
#1) 

class student:
    def __init__(self,name,roll_no,subject1,subject2,subject3):
        self.name = name
        self.roll_no = roll_no 
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
    def display(self):
        print("Student name:-",self.name)
        print("Roll_no:-",self.roll_no)
        print("marks:-",self.subject1,self.subject2,self.subject3)
    def calculate(self):
        total = self.subject1 + self.subject2 + self.subject3 
        print("Total marks:-",total)
        percentage = total /300*100
        print("percentage:-",percentage)
        if percentage >= 40 and self.subject1 >=35 and self.subject2 >= 35 and self.subject3 >= 35:
            print("Result:-PASS")
        else:
            print("Result:-FAILED")


A = student("vedd",11,55,88,87)
A.display()
A.calculate()
print("~~~~~~~~~~~~~~~~~~~~~~~")

B = student("mahi",11,55,90,87)
B.display()
B.calculate()
print("~~~~~~~~~~~~~~~~~~~~~~~")

C = student("sai",11,55,33,87)
C.display()
C.calculate()


print("2)=================================")
#2)


class Bankaccount:
    def __init__(self,__balance):
        self.__balance = __balance
        print("Account Balance:-",self.__balance)
    def deposite(self,amount):
        self.__balance += amount
        print("Total Balance:-",self.__balance)
    def withdrow(self,amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance


py = Bankaccount(1000)
py.deposite(500)
py.withdrow(100)
print("Remaining Balance:-",py.get_balance())

print("------------------------")

py1 = Bankaccount(10000)
py1.deposite(5000)
py1.withdrow(1000)
print("Remaining Balance:-",py.get_balance())


print("3)=================================")


class employee:
    def __init__(self,name,id,salary,):
        self.name =  name
        self.id = id 
        self.salary = salary
        print("Employee Name:-",self.name)
        print("Employee ID:-",self.id)
        print("Employee Salary:-",self.salary)
    def final_salary(self):
        f_salary = self.salary *20/100
        print("Employee HRA salary:-",f_salary)
        b_salary = self.salary *10/100
        print("Employee Bonous salary:-",b_salary)
        Total_Salary =self.salary + f_salary + b_salary
        print("Employee Total Salary:-",Total_Salary)

b1 = employee("adi",11,50000)
b1.final_salary()


print("4)=================================")

class calculatoer:
    @staticmethod
    def addition(a,b):
        return a+b
        print("")
    def substraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        if b==0:
            print("zero division is occur")
        else:
            return a/b

print(calculatoer.addition(10,20))
print(calculatoer.substraction(50,20))
print(calculatoer.multiplication(10,20))
print(calculatoer.division(10,2))


print("5)=================================")

class employee:
    def __init__(self,salary):
        self.salary = salary
    def em_salary(self):
        if 15000 <= self.salary:
            print("salary is accepted")
        else:
            print("salary is rejected")

s1 = employee(19000)
s1.em_salary()

print("6)=================================")

