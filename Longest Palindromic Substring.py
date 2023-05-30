class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return ''
    #     longest_pal = ''
    #     for i in range(len(s)):
    #         len_prefix = len(longest_pal)
    #         temp_pal = s[i:len(longest_pal) + i]
    #         if len_prefix + i > len(s):
    #             break
    #         for c in range(i+len_prefix, len(s)):
    #             temp_pal += s[c]
    #             print(temp_pal)
    #             if temp_pal == temp_pal[::-1] and len(temp_pal) > len(longest_pal):
    #                 longest_pal = temp_pal
    #     return longest_pal

    def longestPalindrome(self, s: str) -> str:
        sub = ''
        for indi, i in enumerate(s):
            print(indi, i)
            for indj, j in enumerate(s[indi:], start=indi):
                if i == j and s[indi:indj + 1] == s[indi:indj + 1][::-1] and len(s[indi:indj + 1]) > len(sub):
                    sub = s[indi:indj + 1]
        return sub

s = "bb"

obj = Solution()
print(f'longest {obj.longestPalindrome(s)}')
