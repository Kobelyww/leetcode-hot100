"""
LeetCode 1. 两数之和 (Two Sum)

题目描述：
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，
并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1:
输入: nums = [2,7,11,15], target = 9
输出: [0,1]
解释: 因为 nums[0] + nums[1] == 9，返回 [0, 1]。

示例 2:
输入: nums = [3,2,4], target = 6
输出: [1,2]

示例 3:
输入: nums = [3,3], target = 6
输出: [0,1]

提示:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- 只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表法（一轮遍历）

        核心思路：
        遍历数组，对于当前数字 num，需要的配对数字是 target - num。
        检查这个配对数字是否已经在哈希表（seen）中：
        - 在：直接返回 [配对数字的下标, 当前下标]
        - 不在：把当前数字和下标存入 seen，继续遍历

        为什么只需一轮？因为 a + b = target，遍历到 b 时 a 一定已经存进去了。

        时间复杂度 O(n)，空间复杂度 O(n)
        """
        seen = {}                             # 值 → 下标，存所有已遍历过的数字
        for i, num in enumerate(nums):
            complement = target - num         # 能和 num 配对的数字
            if complement in seen:            # 之前出现过，找到答案
                return [seen[complement], i]
            seen[num] = i                     # 没找到，存入当前数字供后续使用
        return []                             # 题目保证有解，不会执行到这里


    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []                             # 题目保证有解，不会执行到这里


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]

    # 示例 2
    assert s.twoSum([3, 2, 4], 6) == [1, 2]

    # 示例 3
    assert s.twoSum([3, 3], 6) == [0, 1]

    # 额外测试：负数
    assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # 额外测试：较大数组
    assert s.twoSum([10, 20, 30, 40, 50], 60) == [1, 3]  # 20 + 40 = 60

    print("✅ 所有测试用例通过！")