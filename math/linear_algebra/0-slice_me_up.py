#!/usr/bin/env python3
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]

# Slicing the array correctly
arr1 = arr[0:2]  # First two elements (indices 0 and 1)
arr2 = arr[-5:]  # Last five elements
arr3 = arr[1:6]  # 2nd to 6th elements (indices 1 through 5)

# Printing the results
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))

