"""
1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/
Status: Accepted · 66/66 test cases · solved Nov 1, 2026

Approach: store each number's index in a dictionary. For every number,
check if its complement (target - number) was already seen.

Time: O(n) · Space: O(n)
"""


class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(Solution().twoSum([3, 2, 4], 6))        # [1, 2]
