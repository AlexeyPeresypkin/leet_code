class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


obj = Solution()
s = "   fly me   to   the moon  "
print(obj.lengthOfLastWord(s))
