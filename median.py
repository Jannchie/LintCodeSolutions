class Solution:
    """
    @param: : A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        nums.sort()
        return nums[int((len(nums)-1)/2)]