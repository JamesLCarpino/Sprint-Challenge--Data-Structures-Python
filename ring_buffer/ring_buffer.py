class RingBuffer:
    def __init__(self, capacity=[]):
        self.capacity = capacity

    def append(self, item):
        self.capacity.append(item)

    def get(self):
        pass
