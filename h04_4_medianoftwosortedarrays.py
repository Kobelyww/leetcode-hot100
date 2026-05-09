"""
LeetCode 4. 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)

题目描述：
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的中位数。
算法的时间复杂度应该为 O(log(m + n))。

示例 1:
输入: nums1 = [1,3], nums2 = [2]
输出: 2.00000
解释: 合并数组 = [1,2,3]，中位数 2

示例 2:
输入: nums1 = [1,2], nums2 = [3,4]
输出: 2.50000
解释: 合并数组 = [1,2,3,4]，中位数 (2 + 3) / 2 = 2.5

提示:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        二分查找分割位置

        核心思路：
        中位数将合并后的数组平分为左、右两部分。在 nums1 中找一个分割点 i，
        则 nums2 的分割点 j 也随之确定（j = 总左半元素数 - i）。

        正确的分割满足交叉比较条件：
        - nums1 左半最大值（left1） <= nums2 右半最小值（right2）
        - nums2 左半最大值（left2） <= nums1 右半最小值（right1）

        不满足时用二分调整 i：left1 > right2 说明 i 太大，反之 i 太小。

        关键细节：
        - 始终在较短的数组上二分，保证时间复杂度 O(log(min(m,n)))
        - 越界处理：分割线在数组边界时，用正负无穷代替不存在的元素
        - 奇数长度：中位数 = max(左半); 偶数长度：中位数 = (max(左) + min(右)) / 2

        时间复杂度 O(log(min(m, n)))，空间复杂度 O(1)
        """
        # 保证 nums1 是较短的数组，二分查找代价更小
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2          # 左半部分应包含的元素个数（奇数时左半多一个）
        left, right = 0, m                     # 在 nums1 上二分，i 的取值范围 [0, m]

        while left <= right:
            i = (left + right) // 2            # nums1 分割位置（i 个元素在左半）
            j = total_left - i                 # nums2 分割位置（由 i 决定）

            # 分割线左右的四个值，下标越界时用无穷代替
            left1  = nums1[i - 1] if i > 0 else float('-inf')   # nums1 左半最大值
            right1 = nums1[i]     if i < m else float('inf')      # nums1 右半最小值
            left2  = nums2[j - 1] if j > 0 else float('-inf')   # nums2 左半最大值
            right2 = nums2[j]     if j < n else float('inf')      # nums2 右半最小值

            if left1 <= right2 and left2 <= right1:  # 找到正确的分割
                if (m + n) % 2 == 1:                 # 总数为奇数：中位数 = 左半最大值
                    return max(left1, left2)
                else:                                # 总数为偶数：中位数 = (左max + 右min) / 2
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:               # nums1 左半太大，分割线左移
                right = i - 1
            else:                              # left2 > right1，nums1 左半太小，分割线右移
                left = i + 1

        return 0.0                             # 不会执行到这里（题目保证有解）

    def mysolution(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            left1  = nums1[i - 1] if i > 0 else float('-inf')   # nums1 左半最大值
            right1 = nums1[i]     if i < m else float('inf')      # nums1 右半最小值
            left2  = nums2[j - 1] if j > 0 else float('-inf')   # nums2 左半最大值
            right2 = nums2[j]     if j < n else float('inf')      # nums2 右半最小值

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1

        return 0.0


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert abs(s.findMedianSortedArrays([1, 3], [2]) - 2.0) < 1e-5

    # 示例 2
    assert abs(s.findMedianSortedArrays([1, 2], [3, 4]) - 2.5) < 1e-5

    # 额外测试：一个数组为空
    assert abs(s.findMedianSortedArrays([], [1]) - 1.0) < 1e-5

    # 额外测试：奇数总长度
    assert abs(s.findMedianSortedArrays([1, 2, 3], [4, 5]) - 3.0) < 1e-5

    # 额外测试：相同元素
    assert abs(s.findMedianSortedArrays([1, 1], [1, 1]) - 1.0) < 1e-5

    # 额外测试：nums1 完全小于 nums2
    assert abs(s.findMedianSortedArrays([1, 2], [3, 4, 5]) - 3.0) < 1e-5

    print("✅ 所有测试用例通过！")