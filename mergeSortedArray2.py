class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for Bi in range(0,len(B)):
            for Ai in range(0,len(A)):
                
                if Ai >= m and A[Ai] == 0:
                    A[Ai] = B[Bi]
                    break
                if A[Ai] != None and B[Bi] > A[Ai]:
                    continue
                if B[Bi] < A[Ai]:
                    l = list(range(Ai,len(A)-1))
                    l.reverse()
                    for i in l:
                        A[i + 1] = A[i]
                    A[Ai] = B[Bi]
                    break
        return A
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(n):
            A[m+i] = B[i]
        A.sort()
        return A             