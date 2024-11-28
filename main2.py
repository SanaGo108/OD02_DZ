class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("front from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Пример использования очереди
queue = Queue()
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(9)
print(queue.dequeue())  # Вывод: 1
print(queue.front())    # Вывод: 2