# Leetcode problem 14 (Longest Common Prefix): https://leetcode.com/problems/longest-common-prefix/
# Level: Easy

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        if len(strs) < 2:
            # since the question says there must be one element in the array
            return strs[0]

        first, rest = strs[0], strs[1:]
        for idx, char in enumerate(first):
            for item in rest:
                if idx >= len(item) or char != item[idx]:
                    return common
            common += char
        return common


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(strs=["ab", "a"]) == "a"
    assert solution.longestCommonPrefix(strs=["flower", "flower", "flower"]) == "flower"
