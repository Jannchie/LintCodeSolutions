class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        for n in str:
            a = str.index(n)
            if str.count(str[a]) > 1:
                return False
        return True

# s = Solution()
# print(s.isUnique("abc_______"))