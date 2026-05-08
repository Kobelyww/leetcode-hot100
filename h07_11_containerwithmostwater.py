"""
LeetCode 11. 盛最多水的容器 (Container With Most Water)
Hot 100 #7

题目描述：
给定一个长度为 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

示例 1:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
解释: 选择索引 1 和 8（高度为 8 和 7），宽度为 7，容量 = min(8,7) * 7 = 49

示例 2:
输入: height = [1,1]
输出: 1

提示:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针法

        核心思路：
        左右指针分别从数组两端开始。容量 = min(height[l], height[r]) * (r - l)。
        每次移动较矮的指针（因为宽度在缩小，只有增加高度才可能得到更大容量）。

        关键细节：
        - 为什么移动较矮的指针？因为容量受限于较矮的一边。如果移动较高的一边，
          宽度变小后容量只可能更小（新高度 ≤ 原来的较矮高度）。
        - 移动较矮的一边至少有机会遇到更高的线，从而增加容量。

        时间复杂度 O(n)，空间复杂度 O(1)
        """
        l, r = 0, len(height) - 1              # 左右指针，从最宽开始
        max_water = 0

        while l < r:
            h = min(height[l], height[r])       # 容器高度 = 两端较矮线
            w = r - l                           # 容器宽度
            max_water = max(max_water, h * w)

            if height[l] < height[r]:           # 移动较矮的一边
                l += 1
            else:
                r -= 1

        return max_water


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # 示例 2
    assert s.maxArea([1, 1]) == 1

    # 额外测试：递增
    assert s.maxArea([1, 2, 3, 4, 5]) == 6

    # 额外测试：相同高度
    assert s.maxArea([4, 4, 4, 4]) == 12

    print("✅ 所有测试用例通过！")