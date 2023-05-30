import itertools


class Solution:

    @staticmethod
    def get_position(max_pos):
        while True:
            for i in range(1, max_pos + 1):
                yield i
            for i in reversed(range(2, max_pos)):
                yield i

    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        cy = self.get_position(numRows)
        array = list(itertools.islice(cy, len_s))
        data = {i: '' for i in range(1, numRows + 1)}
        for num, item in enumerate(s):
            data[array[num]] += item
        return ''.join([value for value in data.values()])

    def convert(self, s: str, numRows: int) -> str:
        list_of_items = [[] for i in range(numRows)]
        DOWN = -1
        i = 0
        if numRows == 1:
            return s
        for char in s:
            list_of_items[i].append(char)
            if i == 0 or i == numRows - 1:
                DOWN *= -1
            i += DOWN
        list_of_items = list(itertools.chain(*list_of_items))
        return ''.join(list_of_items)


s = 'PAYPALISHIRING'
obj = Solution()
print(obj.convert(s, 3))
