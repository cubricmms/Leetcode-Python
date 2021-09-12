# Leetcode problem 8 (String to Integer (atoi)): https://leetcode.com/problems/string-to-integer-atoi/
# Level: Medium


class Solution:
    def myAtoi(self, s: str) -> int:
        neg_sign = False
        output = ""
        leading, target = True, False

        for i in range(len(s)):
            current_char = s[i]
            if leading:
                if current_char == " ":
                    continue

                if current_char == "+":
                    leading = False
                    target = True
                    continue
                elif current_char == "-":
                    neg_sign = True
                    leading = False
                    target = True
                    continue

                if current_char.isdigit():
                    output += current_char
                    leading = False
                    target = True
                    continue

                # leading wrong chars
                return 0

            if target:
                if current_char.isdigit():
                    output += current_char
                else:
                    break

        return (
            0
            if not output
            else min(max(-(2 ** 31), int(output) * [1, -1][neg_sign]), (2 ** 31 - 1))
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.myAtoi(s="42") == 42
    assert solution.myAtoi(s="   -42") == -42
    assert solution.myAtoi(s="words and 987") == 0
    assert solution.myAtoi(s="4193 with words") == 4193
    assert solution.myAtoi(s="-91283472332") == -2147483648
