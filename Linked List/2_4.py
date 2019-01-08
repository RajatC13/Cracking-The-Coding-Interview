class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    while(head != None):
        print(head.value)
        head = head.next

def split(head, p):
    h = Node(None)

    t = Node(None)
    h.next = t

    while(head != None):
        if head.value < p:
            if h.value == None:
                h.value = head.value
            else:
                new = Node(head.value)
                new.next = h
                h = new
        else:
            if t.value == None:
                t.value = head.value
            else:
                end = Node(head.value)
                end.next = None
                t.next = end
                t = end
        head = head.next
    return(h)


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

    print_linked_list(split(a, 7))
