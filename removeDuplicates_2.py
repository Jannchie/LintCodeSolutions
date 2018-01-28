class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        i = 0
        while (i < len(nums) - 1): # len(nums) => len(nums)-1
            if i != len(nums) - 2 and nums[i] == nums[i + 1] and nums[i] == nums[i + 2]: # 允许重复两次
                nums.pop(i)
                continue
            i = i + 1
        return len(nums)