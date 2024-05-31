class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0 or s[0] in [']', ')', '}']:
            return False
        map = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        opening = ['{', '(', '[']
        stack = []
        for x in s:
            if x in opening:
                stack.append(x)
            else:
                if len(stack) != 0 and map[stack[-1]] == x:
                    stack.pop()
                else:
                    return False
        return False if len(stack) > 0 else True


ans = Solution().isValid("{[]")
print(ans)
