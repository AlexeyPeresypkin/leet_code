class Solution:
    def myAtoi(self, s: str) -> int:
        max_value = 2147483647
        min_value = -2147483648
        s = s.strip()
        if not s:
            return 0
        sign = s[0] if s[0] in '+-' else False
        result = ''
        start_index = 1 if sign else 0
        for char in s[start_index:]:
            if char.isdigit():
                result += char
                continue
            break
        if not result:
            return 0
        if sign:
            result = sign + result
        result = int(result)
        if result > max_value:
            return max_value
        elif result < min_value:
            return min_value
        return result


s = "   -42"
obj = Solution()
print(obj.myAtoi(s))
