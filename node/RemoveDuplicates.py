from ListNode import ListNode
from LinkedListUtil import createLinkedList, printLinkedList

def removeDuplicates(head: ListNode) -> ListNode:
    if head == None:
        return head
    
    tmp = head

    while tmp != None:
        next = tmp.next

        while next != None and tmp.val == next.val:
            next = next.next

        tmp.next = next
        tmp = tmp.next

    return head

nodes = createLinkedList([1,1,2,3,3])
print("Before")
printLinkedList(nodes)
removeDuplicates(nodes)
print("After")
printLinkedList(nodes)