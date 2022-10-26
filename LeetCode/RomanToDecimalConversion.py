class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        s=input("Enter Roman")

        s.replace("IV", "IIII")
        s.replace("IX", "VIIII")
        s.replace("XL", "XIIII")
        s.replace("XC", "LIIII")
        s.replace("CD", "CCCC")
        s.replace("DM", "DCCCC")

        for char in s:
            output = output + map[char]
        return output
