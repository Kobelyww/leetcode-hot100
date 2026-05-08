"""
LeetCode 2. 两数相加 (Add Two Numbers)

题目描述：
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1:
输入: l1 = [2,4,3], l2 = [5,6,4]
输出: [7,0,8]
解释: 342 + 465 = 807

示例 2:
输入: l1 = [0], l2 = [0]
输出: [0]

示例 3:
输入: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出: [8,9,9,9,0,0,0,1]

提示:
- 每个链表中的节点数在范围 [1, 100] 内
- 0 <= Node.val <= 9
- 题目数据保证列表表示的数字不含前导零
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        解法1：模拟竖式加法（哨兵节点 + 进位变量）

        核心思路：
        链表逆序存储（头=个位），和手写加法从低位往高位算的顺序完全一致。
        同时遍历两个链表，对应位相加再加上进位 carry，用 %10 取当前位，用 //10 算进位。

        关键细节：
        - dummy（哨兵节点）：让结果链表的构建统一化，不需要特殊处理头节点
        - while 条件里的 carry：即使两个链表都空了，如果还有进位（如 999+1），
          需要继续生成一个值为 1 的节点

        时间复杂度 O(max(m, n))，空间复杂度 O(1)（不计返回结果）
        """
        dummy = ListNode()                     # 哨兵节点，真正的结果挂在它后面
        cur = dummy                            # 游标，指向当前结果链表的尾部
        carry = 0                              # 进位（0 或 1）

        while l1 or l2 or carry:               # 只要有数字没处理完 或 还有进位
            val1 = l1.val if l1 else 0         # l1 当前位的值（空了就当 0）
            val2 = l2.val if l2 else 0         # l2 当前位的值（空了就当 0）
            total = val1 + val2 + carry        # 三位相加：l1位 + l2位 + 上轮进位
            carry = total // 10                # 新的进位（整数除法）
            cur.next = ListNode(total % 10)     # 当前位只保留个位
            cur = cur.next                     # 游标后移
            if l1:
                l1 = l1.next                   # l1 指针后移
            if l2:
                l2 = l2.next                   # l2 指针后移

        return dummy.next                      # 跳过哨兵，返回真正的结果链表

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        解法2：另一种模拟进位写法（先占位再填值）

        与解法1的区别：
        - 解法1：计算 total 后直接创建节点，追加到链表尾部
        - 解法2：先创建 ans 节点（占位），计算时直接在 ans 上累加填值；
          如果还需要处理下一位，再创建下一个占位节点

        关键点：
        - ans 是游标（当前正在填值的节点），每轮先在 ans.val 上累加进位和 l1、l2 的值
        - ans1 始终指向头节点，最后返回 ans1 就是整条结果链表
        - 提前创建下个占位节点的逻辑：仅当还有数字或进位时才创建，
          否则 while 循环自然结束，不会产生多余的节点

        时间复杂度 O(max(m, n))，空间复杂度 O(1)（不计返回结果）
        """
        one = 0                                # 进位（0 或 1）
        ans = ListNode(0, None)               # 哨兵/占位节点（第一个结果节点）
        ans1 = ans                             # 记住头节点，最后返回它
        while l1 or l2 or one:                 # 还有数字或进位 → 继续
            ans.val = one                      # 先填入上一轮的进位
            one = 0                            # 进位已使用，清零
            if l1:
                ans.val += l1.val              # 累加 l1 当前位的值
                l1 = l1.next
            if l2:
                ans.val += l2.val              # 累加 l2 当前位的值
                l2 = l2.next
            if ans.val >= 10:                  # 溢出（≥10），产生进位
                one = 1
                ans.val -= 10                  # 当前位只保留个位（减10等效于%10）
            if l1 or l2 or one:                # 还有后续工作 → 创建下一个占位节点
                nxt = ListNode(0, None)
                ans.next = nxt                 # 当前节点连接下一个节点
                ans = nxt                      # 游标移到下一个节点（填值目标）
        return ans1                            # ans1 始终指向头节点


# ========== 辅助函数 & 测试用例 ==========
def build_list(arr):
    """将数组转换为链表"""
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_array(head):
    """将链表转换为数组"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    s = Solution()

    for method in [s.addTwoNumbers, s.addTwoNumbers2]:
        # 示例 1
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])
        assert to_array(method(l1, l2)) == [7, 0, 8]

        # 示例 2
        l1 = build_list([0])
        l2 = build_list([0])
        assert to_array(method(l1, l2)) == [0]

        # 示例 3
        l1 = build_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_list([9, 9, 9, 9])
        assert to_array(method(l1, l2)) == [8, 9, 9, 9, 0, 0, 0, 1]

        # 额外测试：不等长链表
        l1 = build_list([1, 8])
        l2 = build_list([0])
        assert to_array(method(l1, l2)) == [1, 8]

    print("✅ 所有测试用例通过！")