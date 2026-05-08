"""
LeetCode 15. 三数之和 (3Sum)
Hot 100 #8

题目描述：
给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k，同时还满足 nums[i] + nums[j] + nums[k] == 0。
请你返回所有和为 0 且不重复的三元组。

示例 1:
输入: nums = [-1,0,1,2,-1,-4]
输出: [[-1,-1,2],[-1,0,1]]
解释:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
不同的三元组是 [-1,0,1] 和 [-1,-1,2]

示例 2:
输入: nums = [0,1,1]
输出: []

示例 3:
输入: nums = [0,0,0]
输出: [[0,0,0]]

提示:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        排序 + 双指针法

        核心思路：
        先排序，然后固定第一个数 nums[i]，在 i 右侧使用双指针寻找两数之和 = -nums[i]。
        这样就把 3Sum 转化成了对每个 i 的 Two Sum II（有序数组的两数之和）。

        关键细节——去重：
        - 固定数去重：如果 nums[i] == nums[i-1]，跳过（已经找过同样的 target）
        - 双指针去重：找到一组解后，左右指针跳过所有重复值

        时间复杂度 O(n^2)，空间复杂度 O(1)（不计返回结果）
        """
        nums.sort()                            # 排序是双指针的前提
        n = len(nums)
        res = []

        for i in range(n - 2):                 # 固定第一个数（至少留两个位置给左右指针）
            if nums[i] > 0:                    # 最小的数 > 0，不可能三数和为 0
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的固定数
                continue

            target = -nums[i]                  # 需要在右侧找到两数之和 = target
            l, r = i + 1, n - 1                # 双指针区间 [i+1, n-1]

            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:                          # 找到一组解
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  # 跳过左侧重复
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:  # 跳过右侧重复
                        r -= 1

        return res


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    def normalize(result):
        """排序以便比较"""
        return sorted([sorted(triplet) for triplet in result])

    # 示例 1
    result1 = s.threeSum([-1, 0, 1, 2, -1, -4])
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert normalize(result1) == normalize(expected1)

    # 示例 2
    assert s.threeSum([0, 1, 1]) == []

    # 示例 3
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]

    # 额外测试：全正数
    assert s.threeSum([1, 2, 3, 4, 5]) == []

    # 额外测试：大量重复
    result5 = s.threeSum([0, 0, 0, 0])
    assert normalize(result5) == [[0, 0, 0]]

    print("✅ 所有测试用例通过！")