class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.queue = []

    def append(self, item):
        # if the queue is smaller than capacity (5 in this)
        if len(self.queue) < self.capacity:
            # add the item to the back
            self.queue.append(item)
        else:
            # replace oldest value; self.queue[0] = first in queue
            self.queue[self.index] = item
            # Increment the index for added item(s)
        self.index += 1
        # If index +1 brings you over capacity
        if self.index == self.capacity:
            # Reset the index
            self.index = 0

    def get(self):
        # return all elements in given order
        return self.queue