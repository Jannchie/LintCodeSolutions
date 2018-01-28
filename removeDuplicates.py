class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        i = 0
        while(i < len(nums)):
            if i != len(nums) - 1 and nums[i] == nums[i+1]:
                nums.pop(i) # 原先用nums.remove(nums[j])，极慢
                continue
            i = i + 1
        return len(nums)