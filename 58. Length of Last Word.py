class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        first_empty = 0
        lastWord = ""
        for i in range(N - 1, -1, -1):
            if s[-1] == " ":
                if s[i] == " " and first_empty == 0:
                    continue
                elif s[i] != " " and first_empty == 0:
                    first_empty += 1
                    lastWord += s[i]
                elif s[i] == " " and first_empty == 1:
                    return len(lastWord)
                else:
                    lastWord += s[i]
            else:
                if s[i] != " " and first_empty == 0:
                    first_empty += 1
                    lastWord += s[i]
                elif s[i] == " " and first_empty == 1:
                    return len(lastWord)
                else:
                    lastWord += s[i]
        return len(lastWord)


solution = Solution()
print(solution.lengthOfLastWord(""))
