class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        counter0 = 0
        counter1 = 0
        counter2 = 0
        for num in nums:
            if num == 0:
                counter0 +=1
            elif num == 1:
                counter1 +=1
            elif num == 2:
                counter2 +=1
        for n in range(0,counter0):
            nums[n] = 0
        for n in range(counter0,counter0+counter1):
            nums[n] = 1
        for n in range(counter0+counter1,counter0+counter1+counter2):
            nums[n] = 2

s = Solution()
a = [1,2,2,1,2,0,0]
s.sortColors(a)
