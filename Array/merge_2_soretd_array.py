"""
There given two sorted array arr1 and arr2 merge them with out using extra space
INPUT
arr1 = [1,3,5,7] 
arr2 = [0,2,6,8,9]

OUTPUT
merged = [0,1,2,3,5,6,7,8,9]
"""

"""
Its a Two-Pointer Method and uses merge sort algorithm
Lets Undertsnad the Merge sort algo

--- divide and conqure 

[ take the mid value split into left and right

    mid = len(arr) // 2
    left_half = arr[ :mid]
    rigth_half = arr[ mid: ]

]

--- recursively call the merge_sort function

[ sort the left and right halves by calling merge_sort recursively on them 

    left_sorted = merge_sort(left_half)
    rigth_sorted = merge_sort(rigth_half)
    
]

--- merge the two sorted halves into one sorted array

[store them in a result

    sorted_merge = merge(left_sorted, right_sorted)
]
 
"""
""""
logic here is we need to find the smallest elem by comparing both the arrays 
find the smallest elem append it to merged list and iterate through
"""

def merge(a,b):
  i = j = 0
  merged = [ ]
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      merged.append(a[i])
      i += 1
    else:
      merged.append(a[j])
      j += 1
    if i < len(a):
      merged.extend(a[i:])
    if j < len(b):
      merged.extend(b[j:])
  return merged

def merge_sort(arr):
  if len(arr) = 0:
    return arr

mid = len(arr) // 2:
left = merge_sort(arr[ :mid])
right = merge_sort(arr[mid:])

sorted_arr = merge(left, rigth)
                  
    
