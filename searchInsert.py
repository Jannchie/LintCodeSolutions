class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        i = 0
        j = len(A)
        while i < j :
            n = (int)(i + j)/2
            if A[n] > target:
               j = n - 1
            elif A[n] < target:
                i = n + 1
            elif A[n] == target:
                return n
        return i;