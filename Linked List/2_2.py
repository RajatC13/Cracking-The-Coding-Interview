class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_k(head, k):
    counter = 0
    curr = head
    back = head
    while(curr != None):
        print(str(back.value) +"---"+ str(curr.value))
        counter += 1
        if counter > k:
            back = back.next
        curr = curr.next
    return(back.value)

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

    print(delete_k(a, 2))
