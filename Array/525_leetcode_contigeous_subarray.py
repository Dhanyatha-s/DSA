# 
"""
Problem Statement: Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
"""
# for better undertsnading the concept using this arr= [0,1,1,1,1,1,1,0,0,0]
class solutions:
  def subarry(self, nums:List[int])-> int:
    """ the given array is the list of 0s and 1s 
    we need to fing the max_len or max window od size of subarray which must has equal no of 0s and 1s
    to that we need the cumulative sum of the array to find max subarray....!
    SO, we are trasforming 0s with -1 to do summations
    """
    transformed = [1 if x ==1 else -1 for x in nums]  # arr = [-1,1,1,1,1,1,-1,-1,-1]

    """ in order to have the max subarry we need to use hash map to store the index and the value of the array
    """

    sum = 0 # initialy the sum will be 0 can use variable as prifix_sum
    max = 0  # max_len

    # TO STORE THE SUM AND IDX OF THE ARRAY TO FIND THE THE SUBARRAY USE HASH MAP
    idx_map = {0: -1}  # intitial index is -1 with sum 0
    start = end = -1

    for i, val in enumerate(transformed):
      sum += val\
      
       """
      idx  val  sum + val   = SUM      max                                                   |
      -1     0                 0        0                                      |
       0    -1  0 + (-1) =    -1           
       1     1  -1 + ( 1) =    0        2    [ 1--> 0 and 1---> 1 ]
       2     1   0 + (1) =     1
       3     1    1 + 1  =     2        -
       4     1    2 + 1 =      3
       5     1    3 + 1 =      4
       6    -1    4 + (-1) =   3
       7    -1    3 + (-1) =   2        4
       8    -1    2 + (-1) =   1        6

      |                         |
      |                         |
      |                         |
      |                         |
      |                         |
      |  1-->  2                |
      |  0 --> 1                | # SINCE WE HAVE 0 IN THA HASH MAP 
      | -1 --> 0                |
      | 0 --> -1                |
      ---------------------------
      
      """
      if sum in idx_map: # if the value of sum is in the hash map whcih means 0 of index 1 is in the hash map already 
        length = i - idx_map[sum] """# so the i is the idx of current elem and idx_map[sum] is ths idx of sum 
        which in this case is -1 and 1 
        since sum is 0 and already there is hash map its index is 1 idx_map[sum] and the existing val=0 and its idx s -1
        so it becomes -1 - 1 = 2 
        now 
     
      |  1 --> 8                |
      |  2 --> 7                |
      |  3 --> 6                | # SINCE WE HAVE 3 IN THA HASH MAP 
      |  4 --> 5                |
      |  3 --> 4                | HERE WITH IDX 4
      |  2 --> 3                |
      |  1 --> 2                |
      |  0 --> 1                | 
      | -1 --> 0                |
      | 0 --> -1                |
      ---------------------------
      AGAin we are gonna do length = i - idx_map[sum]
      length = 6 (idx of current sum 3) - 4  = 2   
      SINCE WE HAVE 2 too 
      same way  2 is in 3rd idx and i is 7th idx
      so 7 - 3 is 4 
      for 8th idx  sum is 1 so i is 8 and idx_map[sum] is 2 
      8-2 is 6 
      so max is 6
        """
        if length > max:
          max = length   # 6 = 6
          start = idx_map[sum] + 1
          end = i
      else:
        idx_map[sum] = i
  return max # 6
    
