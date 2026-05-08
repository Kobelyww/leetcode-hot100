"""
LeetCode 6. Z 字形变换 (Zigzag Conversion)

题目描述：
将一个给定字符串 s 根据给定的行数 numRows，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串："PAHNAPLSIIGYIR"。

示例 1:
输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"

示例 2:
输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3:
输入: s = "A", numRows = 1
输出: "A"

提示:
- 1 <= s.length <= 1000
- s 由英文字母（小写和大写）、',' 和 '.' 组成
- 1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        按行模拟法

        核心思路：
        把 Z 字形看作是“向下走到底，斜向上走回顶”的周期运动。用 numRows 个字符串
        分别收集每一行的字符，遍历 s 时根据当前方向把字符追加到对应行。

        关键细节：
        - numRows == 1 时直接返回原串，否则取余运算会出错（direction 始终为 0）
        - 方向切换条件：当前行到达首行 (row == 0) 或尾行 (row == numRows-1) 时反转

        时间复杂度 O(n)，空间复杂度 O(n)（存储结果）
        """
        if numRows == 1:                       # 只有一行，直接返回原串
            return s

        rows = [''] * numRows                  # 每行一个字符串收集器
        row = 0                                # 当前行下标
        direction = -1                         # 方向：1=向下，-1=向上

        for ch in s:
            rows[row] += ch                    # 当前字符追加到当前行
            if row == 0 or row == numRows - 1:  # 到达边界，反转方向
                direction = -direction
            row += direction                   # 移动到下一行

        return ''.join(rows)                   # 按行拼接即为结果


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

    # 示例 2
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

    # 示例 3
    assert s.convert("A", 1) == "A"

    # 额外测试：单列
    assert s.convert("ABC", 1) == "ABC"

    # 额外测试：行数等于串长
    assert s.convert("ABC", 3) == "ABC"

    print("✅ 所有测试用例通过！")