class Solution:
    """
    @param: s: A string
    @return: the length of last word
    """

    def lengthOfLastWord(self, s):
        # write your code here
        count = 0
        if s == '':
            return count
        for n in range(1, len(s)+1):
            if s[-n] == ' ' and count != 0:
                return count
            if s[-n] == ' ' and count == 0:
                continue
            count += 1
        return count