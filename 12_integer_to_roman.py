# Leetcode problem 12 (Integer to Roman): https://leetcode.com/problems/integer-to-roman/
# Level: Medium


class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""

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
            if num >= value:
                output += roman
                num -= value
            else:
                step -= 1

        return output


if __name__ == "__main__":
    solution = Solution()
    assert solution.intToRoman(num=3) == "III"
    assert solution.intToRoman(num=4) == "IV"
    assert solution.intToRoman(num=9) == "IX"
    assert solution.intToRoman(num=58) == "LVIII"
    assert solution.intToRoman(num=1994) == "MCMXCIV"
