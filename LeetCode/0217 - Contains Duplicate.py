"""
217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/
Status: Accepted · solved Nov 3, 2026

Approach: keep a set of numbers already seen. If the current number is
already in the set, it's a duplicate, so stop and return True.

Time: O(n) · Space: O(n)
One-line alternative: return len(set(nums)) < len(nums)
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


if __name__ == "__main__":
    print(Solution().containsDuplicate([1, 2, 3, 1]))                    # True
    print(Solution().containsDuplicate([1, 2, 3, 4]))                    # False
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
