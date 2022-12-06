class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "O": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s += 'O'
        prefixes = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        integer = 0
        for i in range(len(s) - 1):
            if s[i] + s[i+1] in prefixes:
                integer -= symbols[s[i]]
            else:
                integer += symbols[s[i]]

        return integer