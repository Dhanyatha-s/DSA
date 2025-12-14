"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, 
nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

"""

"""
COMPARISON BETWEEN MERGE SORT 2 SORTED ARRAY AND MERGE SORT SORTED ARRAY

| MERGE 2 SORTED ARRAY || MERGE SORTED ARRAY |
----------------------------------------------
| GIVEN: arr1 and arr2 || GIVEN: num1 & num2 |
| LOGIC: SOrt the array|  LOGIC: given m & n |
| and store the sorted |  as no. of elems,   | 
| array into separate  |  Need to merge into | 
| variable.            |  single array so    |
| RESULT: is           |  RESULT:its not be  | 
| Returned by function |  returned function. |
| CATCH : None         |  CATCH:array has non|
|                      |  real numbers as 0  |


since we have non real number we need to replace them with kth idx in num1 array as it will be the one single sorted array
means its should be stored inside the array nums1 with m + n
"""

class solutions:
  def merge(self, num1: List[int], m, num2: List[int], n) --> List[int]:
    i = j = k = m-1, n-1, m + n -1
    """
    here m anf n are the  number od elem present in the arrays respectively
    num1 has m = 6  and n = 3 
    where as to have its index i is idx of num1 m-1 is (considering only valid real numbers) 2 idxs
    same in j its n-1 = 2 idxs 
    we need to sort the elem inside the array so to do we have k variable
    so k is the result idx m + n - 1  3 + 3 -1 = 5 idx
    In short i= 2 j = 2 k = 5
    """

    while i > 0 and j > 0:
      if num1[i] > num1[j]: # --> compare elems which is bigger add that to num1[k]
        num1[k] = num1[i]
        i -= 1
        """
        compare num1[i] and num2[j]
        nums1 = [1,2,3],  nums2 = [2,5,6], num1[k] = [1,2,3,0,0,0]

        its from backwords so num1[i] = 3 and num2[j]=6 
        6 is bigger add this at the end of num1[k] at the idx 5
        now its [1,2,3,0,0,6]

        compare num1[i] = 3 and num2[j] = 5 
        5 is bigger 
        num1[k] = [1,2,3,0,5,6]

        compare  num1[i] = 3 and num2[j] = 2
        3 is bigger
        num1[k] = [1,2,3,3,5,6]

        comapre num1[i] = 1 and num2[j] = 2
        2 is bigger 
        num1[k] = [1,2,2,3,5,6]
        """
      else:
        num1[k] = num2[j]
        j -= 1
      # leftover elems
    while j >= 0:
      num1[k] = num2[j]
      j -= 1
      k -= 1
    
     
