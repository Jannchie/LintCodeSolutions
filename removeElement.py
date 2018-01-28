class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        l = len(A)
        i = 0
        while i < l:
            if A[i] == elem:
                A.pop(i)
                l = l - 1
                continue
            i = i + 1
        return len(A)