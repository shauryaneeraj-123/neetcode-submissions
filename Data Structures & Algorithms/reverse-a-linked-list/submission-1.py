class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Nothing has been reversed yet
        prev = None

        # Start at the beginning of the list
        curr = head

        # Keep going until we reach the end
        while curr:

            # Save the rest of the list before changing any pointers
            temp = curr.next

            # Reverse the current node's arrow
            curr.next = prev

            # Move prev forward to the current node
            prev = curr

            # Continue with the next unreversed node
            curr = temp

        # prev now points to the new head of the reversed list
        return prev