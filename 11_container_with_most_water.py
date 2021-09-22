# Leetcode problem 11 (Container With Most Water): https://leetcode.com/problems/container-with-most-water/
# Level: Medium

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most, left, right = 0, 0, len(height) - 1

        # move two cursors towards middle
        while left < right:
            area = min(height[left], height[right]) * (right - left)

            if area > most:
                most = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return most


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea(height=[1, 1]) == 1
    assert solution.maxArea(height=[4, 3, 2, 1, 4]) == 16
    assert solution.maxArea(height=[1, 2, 1]) == 2
