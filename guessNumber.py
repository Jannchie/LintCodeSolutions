"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        a = 0
        b = n
        while a <= b:
            c = int((a + b) / 2)
            g = Guess.guess(c)
            if g == 0:
                return c
            elif g == 1:
                #lower
                a = c + 1
            elif g == -1:
                #higher
                b = c
