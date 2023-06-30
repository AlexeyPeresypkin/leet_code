class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:].startswith(needle):
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


obj = Solution()
haystack = "a"
needle = "a"
print(obj.strStr(haystack, needle))
