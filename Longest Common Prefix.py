from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]
        flag = True
        longest_prefix = ''
        first_item = strs[0]
        for i in range(1, len(first_item) + 1):
            tmp_prefix = first_item[:i]
            for item in strs[1:]:
                if not item.startswith(tmp_prefix):
                    flag = False
                    break
            if flag:
                longest_prefix = tmp_prefix
            else:
                break
        return longest_prefix


strs = ["flower", "flow", "flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs))
