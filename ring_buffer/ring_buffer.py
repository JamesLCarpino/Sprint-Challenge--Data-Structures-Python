


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        # need to take the first item
        #if data length is less than the capacity add to the array
        if len(self.data) < self.capacity:
            self.data.append(item)
            return self.data
        # if the data length = the capacity then the item gets put in at index 0
        elif len(self.data) == self.capacity:
            self.data[self.current] = item
            self.current += 1
            # self.data.append(item)


    def get(self):
        return self.data
