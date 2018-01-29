class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        a = x
        b = 0
        while True:
            c = int((a+b)/2)
            if c*c > x:
                a = c
                continue
            elif c*c <= x and (c+1)*(c+1)>x:
                return c
            else:
                b = c + 1
                continue
            