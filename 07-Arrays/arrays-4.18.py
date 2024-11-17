import MyArrays

arr = [7,3,8,5,2]

print('Numbers', MyArrays.arr_seperated(arr))
print('second largest', MyArrays.max(arr, 2))
print('median: ', MyArrays.median(arr))
print('smallest and largest: ', MyArrays.arr_seperated(MyArrays.get_min_max(arr)))
