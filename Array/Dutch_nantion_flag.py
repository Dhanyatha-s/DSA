"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""
class Solutions:
  def dutchNationalFlag(Self, nums: List[int])->None: # Because to store in in-place
    low = 0
    mid = 0
    high = len(nums) -1 

    while mid < high:
      if nums[mid] == 0:
        # swap 
        nums[low], nums[mid] = nums[mid],nums[low]
        low += 1
        mid += 1
      elif nums[mid] == 1:
        mid += 1
      else:
        nums[mid], nums[high] = nums[high],nums[mid]
        high -= 1
    return nums
    
    
  
