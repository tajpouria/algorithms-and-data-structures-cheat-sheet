class MinHeap():
    def __init__(self, cap):
        self.cap = cap
        self.st = [None] * cap
        self.size = 0

    def __str__(self):
        return str(self.st)

    def get_parent_idx(self, i):
        return (i-1)//2
    
    def get_left_idx(self, i):
        return 2*i+1

    def get_right_idx(self, i):
        return 2*i+2

    def has_parent(self, i):
        return self.get_parent_idx(i) >= 0

    def has_left(self, i):
        return self.get_left_idx(i) < self.size

    def has_right(self, i):
        return self.get_right_idx(i) < self.size

    def parent(self, i):
        return self.st[self.get_parent_idx(i)]

    def left(self, i):
        return self.st[self.get_left_idx(i)]

    def right(self, i):
        return self.st[self.get_right_idx(i)]

    @property
    def is_full(self):
        return self.size == self.cap

    def swap(self, i, j):
        st = self.st
        st[i], st[j] = st[j], st[i]

    def insert(self, data, use_recursion=False):
        if type(data) != int:
            raise Exception("The data must be an integer")
        if self.is_full:
            raise Exception("The heap is full")

        i = self.size
        self.st[i] = data
        self.size += 1
        self.heapify_up_loop() if not use_recursion else self.heapify_up_recursion(i)

    def heapify_up_loop(self):
        i = self.size - 1
        while self.has_parent(i) and self.parent(i) > self.st[i]:
            j = self.get_parent_idx(i)
            self.swap(i, j) 
            i = j

    def heapify_up_recursion(self, i):
        if self.has_parent(i) and self.parent(i) > self.st[i]:
            j = self.get_parent_idx(i)
            self.swap(i, j)
            self.heapify_up_recursion(j)

    def remove_min(self, use_recursion=False):
        if self.size == 0:
            raise Exception("The heap is empty")

        data = self.st[0]
        self.swap(0, self.size - 1)
        self.st[self.size - 1] = None
        self.size -= 1
        self.heapify_down_loop() if use_recursion == False else self.heapify_down_recursion(0)
        return data

    def heapify_down_loop(self):
        i = 0
        while self.has_left(i):
            mci = self.get_left_idx(i)
            if self.has_right(i) and self.right(i) < self.left(i):
                mci = self.get_right_idx(i)
            if self.st[i] < self.st[mci]:
                break
            self.swap(i, mci)
            i = mci

    def heapify_down_recursion(self, i):
        mci = i
        if self.has_left(mci) and self.st[mci] > self.left(i):
            mci = self.get_left_idx(i)
        if self.has_right(i) and self.st[mci] > self.right(i):
            mci = self.get_right_idx(i)
        if mci != i:
            self.swap(i, mci)
            self.heapify_down_recursion(mci)

mh = MinHeap(7)
for el in [10, 20, 5, 8, 0, 15, 30]:
    mh.insert(el, use_recursion=True)
    print(mh)

print("## Removing min")

for i in range(2):
    m = mh.remove_min(use_recursion=True)
    print(m, mh) 
