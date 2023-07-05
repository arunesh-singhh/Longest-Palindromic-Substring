class Soluion:
    def longestPalindrome(self, s: str):
        res = ""
        reslen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l>= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l>= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
        return res

# approach-2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            
            if l >= 1 and s1 == s1[::-1]:
                size += 2
                start = l - 1
            elif s2 == s2[::-1]:
                size += 1
                start = l

        return s[start: start + size]
