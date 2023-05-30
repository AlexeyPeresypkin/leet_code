class Solution:
    roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_digits_values = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                           'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def romanToInt(self, s: str) -> int:
        total = 0
        index = 0
        for roman in self.roman_digits:
            while True:
                if s[index:].startswith(roman):
                    total += self.roman_digits_values[roman]
                    index += len(roman)
                    continue
                break
        return total



s = "MMMXLV"
obj = Solution()
print(obj.romanToInt(s))
