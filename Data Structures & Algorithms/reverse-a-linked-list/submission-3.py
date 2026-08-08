class Solution:
    def reverseList(self, head):
        # prev represents the already-reversed part of the list.
        # At the beginning, nothing has been reversed yet.
        prev = None

        # current is the node we are currently processing.
        current = head

        while current:
            # Save the next node BEFORE changing current.next.
            # Otherwise we would lose access to the rest of the list.
            next_node = current.next

            # Reverse the arrow.
            # Instead of pointing forward, current now points backward.
            current.next = prev

            # Move prev forward.
            prev = current

            # Move current forward using the node we saved earlier.
            current = next_node

        # When current becomes None,
        # prev is sitting on the new first node.
        return prev