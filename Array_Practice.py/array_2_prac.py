import numpy as np

#1)
num = np.array([10,20,30,40,50])
print(np.delete(num,2))


#2)
num=np.array([10,20,30])
n=np.array([40,50,60])
print(np.concatenate((num,n)))


#3)
num=np.array([100,40,50,70,80,60,90,10,20,30])
print(np.sort(num))

#4)
num=np.array([10, 0, 20, 0, 30, 0, 40])
print(np.nonzero(num))

#5)
num = np.array([10,20,30,40,50])
print(np.searchsorted(num,35))

#6)
num = np.array([10, 20, 20, 30, 10, 40, 30])
print(np.unique(num))

#7)
num = np.array([10, 0, 20, 0, 30, 40, 0 ])
print(np.count_nonzero(num))

#8)
num=np.array([10,20,30])
print(np.repeat(num,3))

#9)
marks=np.array([ 85, 90, 75, 88, 92])
print(np.sum(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.min(marks))
print(np.max(marks))

#10)
num=np.array([10, 20, 30, 40])
print(num.ndim)
print(num.shape)
print(num.size)
print(num.dtype)
print(num.itemsize)
print(num.nbytes)


#11)
num=np.array([10,20,30])
n=np.array([40,50,60])
print(np.stack((num,n)))


#12)
num = np.array([10,20,30,40])
arr = num.copy()
arr[0]=50
print(num)
print(arr)

#13)
num=np.array([10,20,30])
arr =num.view()
arr[2]=40
print(num)
print(arr)

#14)
num=np.array([100,40,50,70,80,60])
print(num.reshape(2,3))

#15)
num=np.array([10,20,30,40])
print(np.append(num,50))
print(np.insert(num,1,15))

#16)
num=np.array([100,40,50,70,80,60,90,10,20,30])
arr=num.astype(float)
print(arr)
print(arr.dtype)

#17)
arr = np.array([10,20,30])
print(np.repeat(arr,2))
print(np.tile(arr,2))

#18)
marks=np.array([75, 82, 90, 68, 95, 88, 72, 91])
print(np.sum(marks))
ave= np.mean(marks)
print(ave)
print(np.max(marks))
print(np.min(marks))
print(np.median(marks))
if ave >=70:
    print("Average marks are greater than or equal to 75")
else:
    print("Average marks are less than 75")

#19)
num=np.array([ 50, 20, 80, 10, 60, 30])
print(np.sort(num))
print(np.sum(num))
print(np.max(num))
print(np.min(num))
print(np.mean(num))
print(np.unique(num))
print(np.searchsorted(num,45))

#20)
num=np.array([10,20,30,40,50])
l1=num.tolist()
print(l1)
print(type(l1))
for i in l1:
    print(i)

#21)
data=np.array([45, 78, 90, 32, 65, 88, 55, 92, 40, 76 ])
print(np.sum(data))
avr = np.mean(data)
print(avr)
print(np.max(data))
print(np.min(data))
print(np.sort(data))
print(np.median(data))
print(np.unique(data))
print(np.nonzero(data))
print(np.searchsorted(data,70))
if avr >= 60:
    print("Good Performance")
else:
    print("Need Improvement")



#22)
print("Copy")
cp=np.array([ 10, 20, 30, 40, 50])
h=cp.copy()
h[3]=800
print(cp)
print(h)
print("View")
vi=np.array([ 10, 20, 30, 40, 50])
v=vi.view()
v[3]=100
print(vi)
print(v)
print("-----------")


#23
num=np.array([40, 10, 20, 10, 30, 0, 50, 20])
print(num.ndim)
print(num.shape)
print(num.size)
print(num.dtype)
print(num.itemsize)
print(num.nbytes)
print(np.sort(num))
print(np.sum(num))
print(np.max(num))
print(np.min(num))
print(np.mean(num))
print(np.median(num))
print(np.unique(data))
print(np.nonzero(data))
l2=num.tolist()
print(l2)



#24)
arr = np.array([10, 20, 30, 40, 50, 60])
arr = arr.reshape(2, 3)
arr = arr.flatten()
arr = arr.copy()
arr = np.insert(arr, 2, 25)
arr = np.append(arr, 70)
arr = np.delete(arr, 0)
arr = np.sort(arr)
print("Final Array:", arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

#25)
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
arr = np.array(numbers)
print("Original array:", arr)
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Unique values:", np.unique(arr))
print("Non-zero elements:", np.count_nonzero(arr))
new_num = int(input("Enter an additional number: "))
position = np.searchsorted(sorted_arr, new_num)
print("Insertion position:", position)