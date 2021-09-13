# Leetcode problem 9 (Palindrome Number): https://leetcode.com/problems/palindrome-number/
# Level: Easy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Solution suggest, O(1) space
        # When the quotient is smaller than output => half of the integer lenght is reached
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        output = 0
        while x > output:
            output = output * 10 + x % 10
            x = x // 10

        return output == x or output // 10 == x
        # faster than 45.81%, less than 16.20%
        # TODO: find root cause, speed/memory
        # Possible explanation: while loop performance

    def isPalindrome_string_conversion(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        return int(str(x)[::-1]) == x


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(x=-121) == False
    assert solution.isPalindrome(x=10) == False
    assert solution.isPalindrome(x=-101) == False
    assert solution.isPalindrome(x=121) == True
    assert solution.isPalindrome(x=11) == True
