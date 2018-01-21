class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        left = 0
        right = len(nums) - 1 
        
        while True:
            mid = (left + right) / 2

            if nums[mid] == target:
                while mid != 0 and nums[mid] == nums[mid - 1]:
                    mid = mid - 1
                return mid
                
            if right <= left:
                return -1
                
            if nums[mid] > target:
                right = mid - 1
                continue
            if nums[mid] < target:
                left = mid + 1
                continue
            