"""
LeetCode 7. 整数反转 (Reverse Integer)

题目描述：
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−2^31, 2^31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1:
输入: x = 123
输出: 321

示例 2:
输入: x = -123
输出: -321

示例 3:
输入: x = 120
输出: 21

提示:
- -2^31 <= x <= 2^31 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        数学取余法

        核心思路：
        不断取出 x 的最后一位（x % 10），拼接到结果的末尾（rev = rev * 10 + digit）。
        每次取完后 x //= 10 去掉最后一位。

        关键细节——溢出判断（不能存 64 位整数）：
        - 32 位有符号整数范围：[-2147483648, 2147483647]
        - 在 rev 即将 *10 之前，判断当前 rev 是否会溢出
        - 正数：rev > 214748364 时下一轮必定溢出；rev == 214748364 且 digit > 7 时溢出
        - 负数同理，只是上界数字不同（-2147483648 的个位是 8）

        时间复杂度 O(log₁₀(x))，空间复杂度 O(1)
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        rev = 0                                # 存放反转后的结果
        while x != 0:
            # pop：取出最后一位（Python 中负数 % 10 结果为正，需特殊处理）
            digit = x % 10
            if x < 0 and digit > 0:            # 负数修正：-123 % 10 = 7（Python 特性）
                digit -= 10                    # 修正为 -3
            x = int(x / 10)                    # 直接截断式除法（Python 中负数 // 10 是向下取整）

            # 溢出检查（在 rev * 10 之前）
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
            if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and digit < -8):
                return 0

            # push：拼接到结果尾部
            rev = rev * 10 + digit

        return rev


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.reverse(123) == 321

    # 示例 2
    assert s.reverse(-123) == -321

    # 示例 3
    assert s.reverse(120) == 21

    # 额外测试：0
    assert s.reverse(0) == 0

    # 额外测试：溢出（2147483647 反转后溢出）
    assert s.reverse(1534236469) == 0

    # 额外测试：单个数字
    assert s.reverse(5) == 5

    # 额外测试：负数无零
    assert s.reverse(-120) == -21

    print("✅ 所有测试用例通过！")