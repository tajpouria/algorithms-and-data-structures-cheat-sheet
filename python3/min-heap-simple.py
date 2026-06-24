class MinHeap:
    def __init__(self):
        self.h = []

    def append(self, v):
        h = self.h
        h.append(v)
        i = len(h) - 1
        while i > 0 and h[i] < h[(i - 1) // 2]:
            h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
            i = (i - 1) // 2

    def pop(self):
        h = self.h
        if not h:
            raise IndexError("pop from empty heap")
        if len(h) == 1:
            return h.pop()

        r = h[0]
        h[0] = h.pop()
        
        i = 0
        while 2 * i + 1 < len(h):
            s = i  # Reset s to i at the start of every loop level
            
            # Check left child
            if h[2 * i + 1] < h[s]:
                s = 2 * i + 1
            # Check right child
            if 2 * i + 2 < len(h) and h[2 * i + 2] < h[s]:
                s = 2 * i + 2
                
            if i == s:
                break
                
            h[i], h[s] = h[s], h[i]
            i = s

        return r


mh = MinHeap()
for v in [31, 91, 52, 18, 92, 17, 70, 97, 17, 56]:
    mh.append(v)

for v in [17, 17, 18]:
    assert mh.pop() == v, f"Expected {v}"


assert mh.h == [31, 56, 52, 91, 97, 92, 70]
print("All assertions passed perfectly!")
