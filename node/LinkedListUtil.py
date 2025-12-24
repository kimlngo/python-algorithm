from ListNode import ListNode

def createLinkedList(arr) -> ListNode:
    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    tmp = head
    
    for i in range(1, len(arr)):
        tmp.next = ListNode(arr[i])
        tmp = tmp.next

    return head

def printLinkedList(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")