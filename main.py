class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                # If list1's value is smaller, append it to the merged list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
              
                current.next = list2
                
                list2 = list2.next

            # Move 'current' to the newly added node
            current = current.next

        # If there are remaining nodes in list1, append them to the merged list
        if list1:
            current.next = list1
        
        elif list2:
            current.next = list2

        # Return the head of the merged list (skipping the dummy node)
        return dummy.next

#Convert list to a linkedlist
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result



solution = Solution()
list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])
merged_list = solution.mergeTwoLists(list1, list2)
merged_list_as_list = linkedlist_to_list(merged_list)
print(merged_list_as_list)
