# Leetcode problem 2 (add two number): https://leetcode.com/problems/add-two-numbers/
# Level: Easy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return ", ".join([str(self.val), str(self.next)])


def LinkedList(arr):
    if len(arr) > 1:
        return ListNode(val=arr[0], next=LinkedList(arr[1:]))
    else:
        return ListNode(val=arr[0])


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Pythonic and recursive
        overflow, val = divmod(l1.val + l2.val, 10)
        l3 = ListNode(val=val)

        if any((l1.next, l2.next, overflow)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += overflow
            l3.next = self.addTwoNumbers(l1, l2)

        return l3

    def addTwoNumbersTedious(self, l1, l2):
        # This is not pythonic, but faster than any()
        if l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        elif not l1 and not l2:
            return None

        overflow, val = divmod(l1.val + l2.val, 10)

        if overflow:
            if not l1.next:
                l1.next = ListNode(val=overflow)
            elif not l2.next:
                l2.next = ListNode(val=overflow)
            else:
                l1.next.val += overflow

        l3 = ListNode(val=val, next=self.addTwoNumbers(l1.next, l2.next))
        return l3


if __name__ == "__main__":
    solution = Solution()
    print(solution.addTwoNumbers(l1=LinkedList([2, 4, 3]), l2=LinkedList([5, 6, 4])))
    print(solution.addTwoNumbers(l1=LinkedList([0]), l2=LinkedList([0])))
    print(
        solution.addTwoNumbers(
            l1=LinkedList([9, 9, 9, 9, 9, 9, 9]), l2=LinkedList([9, 9, 9, 9])
        )
    )
