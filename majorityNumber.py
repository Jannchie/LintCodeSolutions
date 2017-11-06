class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        for m in range(0,len(nums)):
            count = 0
            for n in range(m+1,len(nums)):
                n == m
                count = count + 1
                if count >len(nums)/2:
                    return n;
        return;

    