class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[0]
        max = nums[0]
        sum = 0
        for n in nums:
            sum = sum + n
            if max < sum:
                max = sum
            if sum < 0:
                sum = 0
        return max