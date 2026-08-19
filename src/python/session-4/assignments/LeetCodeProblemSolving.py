# Here is the question: https://leetcode.com/problems/add-two-numbers/description/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = ListNode(0)
        current_output= output
        current_node1 = l1
        current_node2 = l2
        carry = 0

        while current_node1 is not None or current_node2 is not None or carry > 0:
            if current_node1 is None and current_node2 is not None:
                current_output.next = ListNode((carry + 0 + current_node2.val) % 10)
                carry = (carry + 0 + current_node2.val) // 10
                current_node2 = current_node2.next
            elif current_node2 is None and current_node1 is not None:
                current_output.next = ListNode((carry + current_node1.val + 0) % 10)
                carry = (carry + current_node1.val + 0) // 10
                current_node1 = current_node1.next
            elif current_node1 is None and current_node2 is None:
                current_output.next = ListNode((carry + 0 + 0) % 10)
                carry = (carry + 0 + 0) // 10
            else:
                current_output.next = ListNode((carry + current_node1.val + current_node2.val) % 10)
                carry = (carry + current_node1.val + current_node2.val) // 10
                current_node2 = current_node2.next
                current_node1 = current_node1.next
            current_output = current_output.next
        return output.next

lst1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
lst2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
sol = Solution()
out = sol.addTwoNumbers(lst1, lst2)
while out is not None:
    print(out.val)
    out = out.next