class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy is a fake node before the real answer.
        dummy = ListNode()

        # tail always points to the LAST node
        # currently in our merged list.
        tail = dummy

        # Continue while BOTH lists still have nodes.
        while list1 and list2:

            if list1.val <= list2.val:
                # list1 has the smaller value,
                # so attach that node next.
                tail.next = list1

                # Move list1 forward.
                list1 = list1.next

            else:
                # list2 has the smaller value.
                tail.next = list2
                list2 = list2.next

            # Move tail to the node we just attached.
            tail = tail.next

        # At this point one list has finished.
        # The other list is already sorted,
        # so attach the entire remainder.
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Skip the fake dummy node.
        return dummy.next