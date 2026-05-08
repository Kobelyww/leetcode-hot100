"""
LeetCode 19. 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)
Hot 100 #10

题目描述：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1:
输入: head = [1,2,3,4,5], n = 2
输出: [1,2,3,5]
解释: 删除倒数第 2 个节点（值为 4）

示例 2:
输入: head = [1], n = 1
输出: []

示例 3:
输入: head = [1,2], n = 1
输出: [1]

提示:
- 链表中结点的数目为 sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        双指针法（快慢指针）

        核心思路：
        fast 指针先走 n+1 步，然后 slow 和 fast 同步移动。
        当 fast 到达末尾时，slow 正好在待删除节点的前驱节点上。

        关键细节：
        - 哨兵节点 dummy：处理删除头节点的情况（如链表 [1]，n=1）
        - fast 先走 n+1 步而不是 n 步：确保 slow 落在待删除节点的前驱位置
        - slow.next = slow.next.next 完成删除

        时间复杂度 O(sz)，空间复杂度 O(1)
        """
        dummy = ListNode(0, head)              # 哨兵节点，处理删除头节点的情况
        fast = slow = dummy

        # fast 先走 n+1 步（+1 是因为有 dummy 在前面）
        for _ in range(n + 1):
            fast = fast.next

        # fast 和 slow 同步移动，直到 fast 到末尾
        while fast:
            fast = fast.next
            slow = slow.next                   # slow 最终停在待删除节点的前驱

        # 删除 slow 的下一个节点
        slow.next = slow.next.next
        return dummy.next


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

    # 示例 1
    head = build_list([1, 2, 3, 4, 5])
    assert to_array(s.removeNthFromEnd(head, 2)) == [1, 2, 3, 5]

    # 示例 2
    head = build_list([1])
    assert to_array(s.removeNthFromEnd(head, 1)) == []

    # 示例 3
    head = build_list([1, 2])
    assert to_array(s.removeNthFromEnd(head, 1)) == [1]

    # 额外测试：删除头节点
    head = build_list([1, 2, 3])
    assert to_array(s.removeNthFromEnd(head, 3)) == [2, 3]

    print("✅ 所有测试用例通过！")