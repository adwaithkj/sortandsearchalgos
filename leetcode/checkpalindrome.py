class Solution:
    def checkpalindrome(self, s):

        if list(reversed(s)) == list(s):
            return True
        return False

    def longestPalindrome(self, s: str, d={}) -> str:
        if s in d and d[s] == True:
            return s

        if len(s) == 1:
            return s
        if self.checkpalindrome(s):
            return s

        d[s] = max([self.longestPalindrome(s[1:]),
                   self.longestPalindrome(s[:-1])], key=lambda x: len(x))
        return d[s]


a = Solution()
print(a.longestPalindrome("abbcccbbbcaaccbababcbcabca"))
