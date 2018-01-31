class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        # Write your code here
        if x == 4:
            return 'NO'
        elif x % 3 == 1 or x % 3 == 0 or x % 7 == 0 or x % 7 == 3 or x % 7 == 6:
            return 'YES'
        else:
            return 'NO'