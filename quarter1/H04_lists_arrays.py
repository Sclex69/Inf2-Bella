import random
import time
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


nums = [1, 2, 3, 4, 5]
nums_array = np.array(nums)

print(sum(nums))
print(np.sum(nums_array))



L = list(range(1_000_000))
A = np.array(L)

# List version
start = time.time()
sum_L = sum([x**2 for x in L])
print("List time:", time.time() - start)

# NumPy version
start = time.time()
sum_A = np.sum(A**2)
print("Array time:", time.time() - start)


list_2d = [[1, 2], [3, 4]]
array_2d = np.array([[1, 2], [3, 4]])

print(list_2d[1][1])
print(array_2d[1, 1])

# Try:
print(array_2d.T)






#Ulohy2

#2
def create_random_list_and_array(length=10, max_value=100):
    lst = [random.randint(0, max_value) for _ in range(length)]
    arr = np.array(lst)  # NumPy array z listu
    return lst, arr

lst, arr = create_random_list_and_array(10)
print("List:", lst)
print("Array:", arr)
#3
first_half_list = lst[:len(lst)//2]
first_half_array = arr[:len(arr)//2]
#4
lst[3] = max(lst)
arr[3] = arr.max()
#5
lst_zeros_ones = [0, 1, 0, 1, 1, 0]
arr_zeros_ones = np.array(lst_zeros_ones)

lst_transformed = [(x + 5) * 3 for x in lst_zeros_ones]
arr_transformed = (arr_zeros_ones + 5) * 3
#6
sum_list = sum(lst)
sum_array = arr.sum()
#7
lst_even = list(range(2, 21, 2))  # 2,4,6,...20
arr_even = np.arange(2, 21, 2)
#8
unique_sorted = sorted(set(lst))
second_smallest_list = unique_sorted[1] if len(unique_sorted) > 1 else None
#9
unique_sorted_arr = np.sort(np.unique(arr))
second_smallest_array = unique_sorted_arr[1] if len(unique_sorted_arr) > 1 else None
#10
lst.clear()
arr = np.array([])



