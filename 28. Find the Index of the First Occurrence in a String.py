class Solution:
    def strStr(self, haystack: str, needle: str):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:len(needle)+i] == needle:
                return i
        return -1


solution = Solution()
ss = solution.strStr(haystack="sadbutsad", needle="sad")
print(ss)