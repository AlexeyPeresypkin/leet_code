from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            if i > 2:
                tmp_lst = [1]
                for c in range(1, i - 1):
                    tmp_lst.append(result[-1][c-1] + result[-1][c])
                tmp_lst.append(1)
                result.append(tmp_lst)
            else:
                result.append([1] * i)
        return result


obj = Solution()
print(obj.generate(10))
