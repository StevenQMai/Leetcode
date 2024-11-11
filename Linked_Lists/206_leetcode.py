# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        # Initialize previous pointer as None (nothing before the first node)
        prev = None
        # Start with the current pointer at the head of the list
        current = head
        # Loop until we reach the end of the list (curr becomes None)
        while current:
            # Save the next node (so we don't lose it when we reverse the link)
            next_node = current.next
            # Reverse the current node's link to point to the previous node
            current.next = prev
            # Move the previous pointer to the current node (we're done with it now)
            prev = current
            # Move to the next node in the original list
            current = next_node
        # When we're done, prev will be the new head of the reversed list
        return prev

    

# Step 1: Save the next node
# Step 2: Reverse the pointer
# Step 3: Move 'prev' forward
# Step 4: Move 'current' forward



# Iteration 1 (Current Node = 1):
    # Save the next node:
    # next_node = current.next (which points to node 2)

    # Reverse the pointer:
    # current.next = prev (set node 1’s next to None, since prev is None)

    # Move prev forward:
    # prev = current (now, prev points to node 1)

    # Move current forward:
    # current = next_node (now, current points to node 2)

    # The list now looks like this:
    # 1 -> None


# Iteration 2 (Current Node = 2):
    # Save the next node:
    # next_node = current.next (which points to node 3)

    # Reverse the pointer:
    # current.next = prev (set node 2’s next to node 1)

    # Move prev forward:
    # prev = current (now, prev points to node 2)

    # Move current forward:
    # current = next_node (now, current points to node 3)

    # The list now looks like this:
    # 2 -> 1 -> None