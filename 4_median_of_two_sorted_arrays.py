# Leetcode problem 4 (Median of Two Sorted Arrays):
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Level: Hard


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # TODO: Quick but not that quick, need to reduce the array in each iteration
        "Resort the two arrays, Time: O(m+n)"
        m, n = len(nums1), len(nums2)
        quotient, remainder = divmod(m + n, 2)
        count = quotient + 1
        # if len is Odd, +1 is the solution; else if len is Even, also need one more iteration
        result, current = list(), None
        while count:
            #  Resorting
            if not nums1:
                current = nums2.pop(0)
            elif not nums2:
                current = nums1.pop(0)
            elif nums1[0] <= nums2[0]:
                current = nums1.pop(0)
            else:
                current = nums2.pop(0)

            if count == 1 and remainder:  # Odd
                result.append(current)

            if (count == 2 or count == 1) and not remainder:  # Even
                result.append(current)

            count -= 1

        return sum(result) / float(len(result))


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2.0
    assert solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.5
    assert solution.findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]) == 0.0
    assert solution.findMedianSortedArrays(nums1=[], nums2=[1]) == 1.0
    assert solution.findMedianSortedArrays(nums1=[2], nums2=[]) == 2.0
