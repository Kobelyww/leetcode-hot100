"""
LeetCode 9. 回文数 (Palindrome Number)

题目描述：
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

进阶：你能不将整数转为字符串来解决这个问题吗？

示例 1:
输入: x = 121
输出: true

示例 2:
输入: x = -121
输出: false
解释: 从左向右读, 为 -121 。从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: x = 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

提示:
- -2^31 <= x <= 2^31 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        反转半数数字法（不转字符串）

        核心思路：
        反转数字的后一半，与剩下一半比较。例如 1221，反转后一半得 12，与前一半 12 相等，
        说明是回文数。

        关键细节：
        - 负数和以 0 结尾的数（但 0 自身除外）直接 false
        - 循环条件 `reverted < x`：当 reverted >= x 时，已经处理了原始数字的一半位数
        - 偶数位：1221 → x=12, reverted=12 → x == reverted
        - 奇数位：12321 → x=12, reverted=123 → x == reverted // 10（中间数字 3 不影响）

        时间复杂度 O(log₁₀(x))，空间复杂度 O(1)
        """
        if x < 0 or (x % 10 == 0 and x != 0):  # 负数和末尾为0的数（0除外）不是回文
            return False

        reverted = 0                            # 存储反转的后半部分
        while reverted < x:                     # 只反转一半
            reverted = reverted * 10 + x % 10   # 取出最后一位拼到 reverted 末尾
            x //= 10                            # 去掉最后一位

        # 偶数位 x == reverted；奇数位 x == reverted // 10（去掉中间位）
        return x == reverted or x == reverted // 10


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.isPalindrome(121) == True

    # 示例 2
    assert s.isPalindrome(-121) == False

    # 示例 3
    assert s.isPalindrome(10) == False

    # 额外测试：奇数位回文
    assert s.isPalindrome(12321) == True

    # 额外测试：偶数位回文
    assert s.isPalindrome(1221) == True

    # 额外测试：0
    assert s.isPalindrome(0) == True

    # 额外测试：非回文
    assert s.isPalindrome(123) == False

    print("✅ 所有测试用例通过！")