import numpy as np
print(np.array([1,2,3,4,5]))
mylist = [1,2,3,4,5]
print(mylist)


mylist = [10, 20, 30, 40, 50]
print(mylist [0], mylist [len(mylist)-1])

myarray = np.array([10,20,30,40,50])
print(myarray[0],myarray[len(myarray)-1])

list_a = [1, 2, 3]
array_a = np.array([1, 2, 3])

print(list_a * 2) ##list spravy 2x ten list za sebou a array de vsetko v array 2x
print(array_a * 2)


list_a = [1, 2, 3]
list_b = [4, 5, 6]

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print(list_a + list_b) ##list ich spoji a array ich pripocita
print(array_a + array_b)


my_list = [7, 8, 9]
my_array = np.array([10, 11, 12])
my_list2 = my_array
my_array2 = my_list
print(my_list2)
print(my_array2)