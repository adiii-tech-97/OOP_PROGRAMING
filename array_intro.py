import numpy as np 
# (Import the NumPy library and call it np so I can use its functions easily.)

arr =np.array([10,20,30,40,50])
#(Create a NumPy array using nd.array() function containing 10, 20, 30, 40, 50 and store it in arr.)


'''(-----------------------"Properties of 1D array"----------------------)'''

print(arr)
#(diaplay the given array using print() function)

print(arr.ndim)
#(is used to check the number of dimensions of a NumPy array)

print(type(arr))
#(check the data type )

print(arr.shape)
#(is used to check the shape/structure of a NumPy array.)

print(arr.size)
#(is used to find the total number of elements in a NumPy array.)

print(arr.dtype)
#(What type of data is stored in this NumPy array)

print(arr.itemsize)
#(how many bytes are used to store one element of a NumPy array.)

print(arr.nbytes)
#(total memory used by all elements in a NumPy array)



'''(--------------------"methods of 1D array"---------------------)'''


arr=np.array([10,20,30,40])
new_arr=arr.astype(float)              #(convert the data type of an array)
print(new_arr)
print(new_arr.dtype)


arr=np.array([10,20,30,40])
new_arr=arr.copy()                     #(create an independant copy of the Array)
new_arr[0]=70
print(arr)
print(new_arr)


arr=np.array([10,20,30,40])
new_arr=arr.view()                     #(share the memmor with the origanal array)
new_arr[0]=70
print(arr)
print(new_arr)

arr=np.array([10,20,30,40,50])
l1=arr.tolist()                        #(convert the numpy array into a python list)
print(l1)
print(type(l1))

l1=np.array([10,40,20,50,30,6])
print(l1.reshape(2,3))                 #(change the shape of the array)

l1=np.array([10,40,20,50,30,6])
l1.resize(3,refcheck=False)            #(change the size of existing size)
print(l1)

l1=np.array([[10,40,20],[50,30,6]])
print(l1.flatten())                    #(converts as array into 1D array)

l1=np.array([10,40,20,50,30,6])
print(np.append(l1,55))                #(add element at the end of array  )

l1=np.array([10,40,20,50,30,6])
print(np.insert(l1,3,55))              #(insers the element at a specific index)


arr = np.array([10,20,30,40,50])
print(np.delete(arr,2))                #(remove an element )

a=np.array([10,20])
b=np.array([30,40])
print(np.concatenate((a,b)))          #(join tow or more array)

a=np.array([10,20])
b=np.array([30,40])
print(np.stack((a,b)))                #(create new dementions array)

arr=np.array([90,80,70,60,50,40,30,20,10])
print(np.sort(arr))                   #(sort the array inaccending order)

arr=np.array([10,22,0,89,0,90])
print(np.nonzero(arr))                #(returns indices of non-zero element)

vibe=np.array([10,20,30,40,50])
print(np.searchsorted(vibe,100))      


adi = np.array([90,20,20,70,40,80,10,30,20,40])
print(np.unique(adi))

arr=np.array([10,22,0,89,0,90])
print(np.count_nonzero(arr))

a=np.array([10,20])
print(np.repeat(a,1))

a=np.array([10,20])
print(np.tile(a,5))

marks = np.array([94,85,87,65,57])
print(np.sum(marks))

marks = np.array([94,85,87,65,57])
print(np.mean(marks))

marks = np.array([94,85,87,65,57])
print(np.median(marks))

marks = np.array([94,85,87,65,57])
print(np.max(marks))

marks = np.array([94,85,87,65,57])
print(np.min(marks))


