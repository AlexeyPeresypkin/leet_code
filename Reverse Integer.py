"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0."""


class Solution:

    def is_32_bit(self, number):
        if number > 2147483647 or number < -2147483648:
            return False
        return True

    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            result = int(f'{str(x)[0]}{str(x)[1:][::-1]}')
            if self.is_32_bit(result):
                return result
            return 0
        result = int(str(x)[::-1])
        if self.is_32_bit(result):
            return result
        return 0


x = -2147483648
obj = Solution()
print(obj.reverse(x))
