class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        s = s.replace(' ','')
        s = "".join(i for i in s if i.isalnum()).lower()

        return s[0::] == s[::-1]