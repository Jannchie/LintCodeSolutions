class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        C = list()
        while A or B:
            if A == [] and B != []:
                C.append(B.pop(0))
                continue
            if  B == [] and A != []:
                C.append(A.pop(0))
                continue
            if A[0] > B[0]:
                C.append(B.pop(0))
                continue                
            else:
                C.append(A.pop(0))
        return C

s = Solution()
s.mergeSortedArray([8],[])