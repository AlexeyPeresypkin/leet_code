class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_longest = 0
        start = 0
        end = 1
        while len(s) - start > max_longest:
            if len(s[start:end]) == len(set(s[start:end])):
                max_longest = max(len(s[start:end]), max_longest)
                end += 1
            else:
                start += 1
        return max_longest


s = ""
obj = Solution()
print(obj.lengthOfLongestSubstring(s))