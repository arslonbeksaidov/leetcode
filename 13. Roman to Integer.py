class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        for x in range(0, len(s)-1):
            if roman[s[x]] < roman[s[x+1]]:
                ans -= roman[s[x]]
            else:
                ans += roman[s[x]]
        ans += roman[s[len(s)-1]]
        return ans


ans = Solution().romanToInt("MCMXCIV")
print(ans)