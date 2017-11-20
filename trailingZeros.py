def trailingZeros(self, n):
    # write your code here, try to do it without arithmetic operators.
    count = 0
    while n>=5:
        n /= 5
        count += n
    return count