class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        n = [1]*len(nums)
        i = 0
        while i < len(nums):
            # n[i] = 1
            if i != 0:
                for j in range(0,i):
                    n[i] = n[i] * nums[j]
            if i != len(nums) - 1:
                for k in range(i+1,len(nums)):
                    n[i] = n[i] * nums[k]
            i = i + 1
        return n
        
s = Solution()
s.productExcludeItself([1,2,3,4,5])

