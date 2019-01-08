class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    while(head != None):
        print(head.value)
        head = head.next

def delete_dupe(head):
    prev = None
    curr = head
    a = []
    while(curr != None):
        if(curr.value in a):
            if(prev == None):
                head = curr.next
                curr = head
                curr.next = None
            else:
                prev.next = curr.next
        a.append(curr.value)
        prev = curr
        curr = curr.next
    return head


if __name__ == "__main__":
    a = Node(5)
    b = Node(6)
    c = Node(7)
    d = Node(5)
    e = Node(8)
    f = Node(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = None

    print_linked_list(delete_dupe(a))
