class Solution:
    """
    @pirim: nums: in array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        i = 0
        j = len(nums) - 1
        while True:
            while nums[i] % 2 == 1:
                i = i + 1
            while nums[j] % 2 == 0:
                j = j - 1
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i = i + 1
                j = j - 1
            else:
                break

s = Solution()
nums=[1,2,3,4,5,6]
s.partitionArray(nums)
