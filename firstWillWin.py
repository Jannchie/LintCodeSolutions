class Solution:
    """
    @param: n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n%3 == 0 : return False
        return True
