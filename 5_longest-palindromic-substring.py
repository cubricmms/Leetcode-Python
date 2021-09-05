# Leetcode problem 5 (Longest Palindromic Substring): https://leetcode.com/problems/longest-palindromic-substring/
# Level: Medium


class Solution:
    # TODO: code all 4 solutions to better understand DP and Manacher
    # https://leetcode.com/problems/longest-palindromic-substring/solution/
    def longestPalindrome(self, s: str) -> str:
        # approach 4: expand around center
        m = ""  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j - i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestPalindrome(s="babad") == "bab"
    assert solution.longestPalindrome(s="cabad") == "aba"
    assert solution.longestPalindrome(s="cbbd") == "bb"
    assert solution.longestPalindrome(s="a") == "a"
    assert solution.longestPalindrome(s="ac") == "a"
    assert solution.longestPalindrome(s="abaxabaxabb") == "baxabaxab"
