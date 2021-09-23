# Leetcode problem 13 (Roman to Integer): https://leetcode.com/problems/roman-to-integer/
# Level: Easy


class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0

        roman_map = (
            ("I", 1),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("L", 50),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("D", 500),
            ("CM", 900),
            ("M", 1000),
        )

        step = len(roman_map) - 1

        while step >= 0:
            roman, value = roman_map[step]
            if roman == s[: len(roman)]:
                output += value
                s = s[len(roman) :]
            else:
                step -= 1

        return output


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt(s="III") == 3
    assert solution.romanToInt(s="IV") == 4
    assert solution.romanToInt(s="IX") == 9
    assert solution.romanToInt(s="LVIII") == 58
    assert solution.romanToInt(s="MCMXCIV") == 1994
