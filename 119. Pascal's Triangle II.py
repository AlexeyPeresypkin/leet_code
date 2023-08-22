from typing import List


# l = [1, 8, 28, 56, 70, 56, 28, 8, 1]

# for i in range(len(l)-1):
#     l_new = [l[i]+l[i+1] for i in range(len(l)-1)]
# l_new = [l[i] + l[i + 1] for i in range(len(l) - 1)]
# print(l_new)


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        num = 2
        tmp_list = [1, 1]
        while num < rowIndex + 1:
            tmp_list = [1] + [tmp_list[i] + tmp_list[i + 1] for i in range(len(tmp_list) - 1)] + [1]
            num += 1
        return tmp_list


obj = Solution()
print(obj.getRow(4))
