class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        maxlen = 0
        arraylist = list()
        for word in dictionary:
            if maxlen < len(word):
                maxlen = len(word)
        for word in dictionary:
            if len(word) == maxlen:
                arraylist.append(word)
        return arraylist

    def longestWords_2(self, dictionary):
        maxlen = 0
        arraylist = list()
        for word in dictionary:
            if maxlen < len(word):
                maxlen = len(word)
                arraylist = list()
            if maxlen == len(word):
                arraylist.append(word)
        return arraylist


s = Solution()
s.longestWords_2(
    ["dog", "google", "facebook", "internationalization", "blabla"])
