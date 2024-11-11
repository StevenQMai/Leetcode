# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head):

        def critical(prev, cur, nxt): #determines whether the three nodes (prev, cur and nxt) are critical points or not 
             return (
                prev.val > cur.val < nxt.val or #local min
                prev.val < cur.val > nxt.val #local max
             ) #returns a true or false statement

        prev, cur = head, head.next
        nxt = cur.next
        min_dist, max_dist = float("inf"), float("-inf")
        prev_crit_idx = 0
        first_crit_idx = 0
        i = 1 #index of cur

        while nxt: #continues the while loop while 'nxt', the reference to the next node is not 'None'
            if critical(prev, cur, nxt):
                if first_crit_idx: #if this first critical node index is non-zero
                    max_dist = i - first_crit_idx
                    min_dist = min(
                        min_dist, 
                        i - prev_crit_idx
                    )
                else:
                    first_crit_idx = i
                prev_crit_idx = i

            prev, cur, nxt = cur, nxt, nxt.next #shifts pointers
            i += 1

        if min_dist == float("inf"):
            min_dist = -1
            max_dist = -1

        return [min_dist, max_dist]



head = ListNode(3, ListNode(1))
solution = Solution()
result = solution.nodesBetweenCriticalPoints(head)
print(result)