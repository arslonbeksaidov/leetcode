class Solution(object):
    def isPalindrome(self, x):
        old = str(x)
        if x < 0:
            return False
        ans = ""
        length = len(str(x))
        for i in range(0, length):
            if 9 < x:
                ans += str(x % 10)
                x = x // 10
            else:
                ans += str(x)
        if ans == old:
            return True
        return False


ans = Solution().isPalindrome(121)
print(ans)
