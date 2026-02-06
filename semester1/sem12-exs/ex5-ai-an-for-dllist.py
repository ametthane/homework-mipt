class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, v):
        if self.start_node is None:
            self.start_node = Node(v)
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new = Node(v)
        n.nref = new
        new.pref = n

    def to_list(self):
        a = []
        n = self.start_node
        while n:
            a.append(n.item)
            n = n.nref
        return a

    def pair_diffs(self):
        a = self.to_list()
        n = len(a)
        res = []
        i = 0
        j = n - 1
        while i <= j:
            res.append(a[i] - a[j])
            i += 1
            j -= 1
        return res


s = DoublyLinkedList()
vals = input("Введите элементы двусвязного списка через пробел: ").strip()
if vals:
    for x in vals.split():
        s.insert_at_end(int(x))
print("Список:", s.to_list())
print("Парные разности a1-an, a2-a(n-1), ...:", s.pair_diffs())
