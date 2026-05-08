"""
LeetCode 17. 电话号码的字母组合 (Letter Combinations of a Phone Number)
Hot 100 #9

题目描述：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
数字到字母的映射与电话按键相同（九宫格键盘）。

2: abc   3: def   4: ghi    5: jkl
6: mno   7: pqrs  8: tuv    9: wxyz

示例 1:
输入: digits = "23"
输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2:
输入: digits = ""
输出: []

示例 3:
输入: digits = "2"
输出: ["a","b","c"]

提示:
- 0 <= digits.length <= 4
- digits[i] 是范围 ['2', '9'] 的一个数字
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        回溯法（DFS）

        核心思路：
        每个数字对应 3-4 个字母，用 DFS 枚举所有可能的组合路径。
        递归深度 = 数字个数，每个节点分支 = 该数字对应的字母数。

        时间复杂度 O(4^n)（n 为 digits 长度），空间复杂度 O(n)（递归栈深度）
        """
        if not digits:                         # 空输入直接返回
            return []

        mapping = {
            '2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs','8': 'tuv', '9': 'wxyz'
        }

        res = []

        def backtrack(index: int, path: list):
            """index: 当前处理到的数字下标; path: 当前构建的字符列表"""
            if index == len(digits):           # 所有数字都处理完毕
                res.append(''.join(path))       # 将路径转为字符串加入结果
                return

            for ch in mapping[digits[index]]:   # 遍历当前数字对应的每个字母
                path.append(ch)                 # 做选择
                backtrack(index + 1, path)      # 递归处理下一个数字
                path.pop()                      # 撤销选择（回溯）

        backtrack(0, [])
        return res


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    def check(result, expected):
        return set(result) == set(expected)

    # 示例 1
    assert check(s.letterCombinations("23"),
                 ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    # 示例 2
    assert s.letterCombinations("") == []

    # 示例 3
    assert check(s.letterCombinations("2"), ["a","b","c"])

    # 额外测试：4位数字
    result4 = s.letterCombinations("7")
    assert check(result4, ["p","q","r","s"])

    print("✅ 所有测试用例通过！")