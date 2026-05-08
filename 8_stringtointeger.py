"""
LeetCode 8. 字符串转换整数 (atoi) (String to Integer (atoi))

题目描述：
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
函数需要依次执行以下步骤：

1. 丢弃前导空格
2. 检查第一个字符（如果有）是 '+' 还是 '-'，确定正负号；
   如果两者都不存在，则假定为正
3. 读入字符直到下一个非数字字符或到达字符串末尾，忽略后续内容
4. 如果没有读入任何数字，则整数为 0
5. 如果整数超过 32 位有符号整数范围 [−2^31, 2^31 − 1]，则截断至边界值

示例 1:
输入: s = "42"
输出: 42

示例 2:
输入: s = "   -42"
输出: -42

示例 3:
输入: s = "4193 with words"
输出: 4193

示例 4:
输入: s = "words and 987"
输出: 0

示例 5:
输入: s = "-91283472332"
输出: -2147483648

提示:
- 0 <= s.length <= 200
- s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        模拟法：严格按照题目描述的步骤执行

        核心思路：
        1. 跳过前导空格
        2. 判断正负号
        3. 连续读取数字字符并累加（类似于第 7 题的逐位构建）
        4. 溢出时截断至对应边界

        时间复杂度 O(n)，空间复杂度 O(1)
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        n = len(s)
        i = 0

        # 步骤 1：丢弃前导空格
        while i < n and s[i] == ' ':
            i += 1

        # 步骤 2：判断符号
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 步骤 3 & 4：读取数字并构建整数
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 步骤 5：溢出检查（类似第 7 题）
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.myAtoi("42") == 42

    # 示例 2
    assert s.myAtoi("   -42") == -42

    # 示例 3
    assert s.myAtoi("4193 with words") == 4193

    # 示例 4
    assert s.myAtoi("words and 987") == 0

    # 示例 5
    assert s.myAtoi("-91283472332") == -2147483648

    # 额外测试：正号
    assert s.myAtoi("+1") == 1

    # 额外测试：空串
    assert s.myAtoi("") == 0

    # 额外测试：纯空格
    assert s.myAtoi("   ") == 0

    # 额外测试：边界值
    assert s.myAtoi("2147483647") == 2147483647
    assert s.myAtoi("-2147483648") == -2147483648

    print("✅ 所有测试用例通过！")