from typing import List


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
