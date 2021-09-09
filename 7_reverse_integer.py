# Leetcode problem 7 (Reverse Integer): https://leetcode.com/problems/reverse-integer/
# Level: Easy


class Solution(object):
    def reverse(self, x: int) -> int:
        # boring but robust
        # one hack for picking binary data
        result = [1, -1][x < 0] * int(str(abs(x))[::-1])
        return result if -(2 ** 31) - 1 < result < 2 ** 31 else 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverse(x=123) == 321
    assert solution.reverse(x=-123) == -321
    assert solution.reverse(x=120) == 21
    assert solution.reverse(x=0) == 0
