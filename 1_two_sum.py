# Leetcode problem 1 (two sum): https://leetcode.com/problems/two-sum/
# Level: Easy


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()

        for idx, val in enumerate(nums):
            remain = target - val
            if remain in hashmap:
                return [idx, hashmap[remain]]

            else:
                hashmap[val] = idx


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    print(solution.twoSum(nums=[3, 2, 4], target=6))
    print(solution.twoSum(nums=[3, 3], target=6))
