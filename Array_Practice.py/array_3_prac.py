import numpy as np
'''
SECTION:-1
'''

#1).
sal=np.array([25000, 32000, 28000, 45000, 38000, 52000, 41000, 60000, 35000, 48000])
print(sal[0],sal[2],sal[4],sal[9])

#2).
arr=np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[0:9])
print(arr[::-1])

#3).
arr1=np.array([15, 25, 35, 45, 55, 65, 75, 85])
arr1[1]=50
arr1[4]=70
print(arr1)

#4).
n=np.array([10, 20, 30, 40, 50] )
add=n[1]+n[3]
print("Addition",add)
sub=n[0]-n[3]
print("Subsraction",sub)
mul=n[2]*n[1]
print("multiplication",mul)
div=n[1]/n[4]
print("division",div)
pow=n[2]**n[3]
print("power",pow)


#5).
num=np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(num[0])
print(num[2])
print(num[:,0])
print(num[:,3])

#6).
s=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print(s[1,1,2])
print(s[2,0,0])
print(s[0,1,2])

#7).
a=np.array([10, 20, 30, 40, 50])
print(a+10)

#8).
Array1=np.array([10, 20, 30, 40, 50])
Array2=np.array([2, 4, 5, 8, 10])
add=Array1+Array2
print("Addition",add)
sub=Array1-Array2
print("Subsraction",sub)
mul=Array1*Array2
print("multiplication",mul)
div=Array1/Array2
print("division",div)


#9).
num=np.array([45, 12, 89, 34, 67, 23, 91, 56, 8, 72])
print(num.max())
print(num.min())
print(num.argmax())
print(num.argmin())

#10).
val=np.array([10, 20, 30, 40, 50, 60])
print(val.std())
print(val.var())

#11).
n=np.array([2, 3, 4, 5])
print(np.cumsum(n))
print(np.cumprod(n))

#12).
num=np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
num[0,1]=99
num[1,2]=33
print(num)


#13).
val1=np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
val=np.array([1, 2, 3])
print(val1+val)


#14).
# n1=np.array([10, 20, 30])
# n2=np.array([1, 2])
# print(n1+n2)

'''
SECTION:-2
'''

#1).

NUM=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]],[[130,140,150],[160,170,180]]])
print(NUM[1,1,1])

#2).

num=np.array([[[5,10],[15,20]],[[25,30],[35,40]],[[45,50],[55,60]]])
print(num[1,1,0])


#3).
n=np.array([[[11,22,33],[44,55,66]],[[77,88,99],[111,122,133]]])
print(n[1,1,1])


#4).
val=np.array([[[100,200],[300,400]],[[500,600],[700,800]],[[900,1000],[1100,1200]]])
print(val[-1,-1,-2])

#5).
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr[2,0,1])

#6).
arr=np.array([[[10,20,30],[40,50,60],[70,80,90]],[[100,110,120],[130,140,150],[160,170,180]]])
print(arr[1,2,0])

#7).
num=np.array([[[101,102],[103,104]],[[105,106],[107,108]],[[109,110],[111,112]],[[113,114],[115,116]]])
print(num[-1,-2,-1])

#8)
data=np.array([[[10,20,30,40],[50,60,70,80]],[[90,100,110,120],[130,140,150,160]],[[170,180,190,200],[210,220,230,240]]])
print(data[2,1,2])

#9).
integers=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]])
print(integers[3,0,0])

#10).
val=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]],[[130,140,150],[160,170,180]],[[190,200,210],[220,230,240]]])
print(val[-1,-2,-2])
print(val.ndim)

data=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]],[[130,140,150],[160,170,180]],[[190,200,210],[220,230,240]]])
print(data[-1,-1,-2])

