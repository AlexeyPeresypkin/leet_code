class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = '[({'
        closed_brackets = '])}'
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            elif bracket in closed_brackets and not stack:
                return False
            else:
                last_open_bracket = stack.pop()
                if open_brackets[closed_brackets.index(bracket)] != last_open_bracket:
                    return False
        return True if not stack else False


s = "{[]}()"

obj = Solution()
print(obj.isValid(s))
