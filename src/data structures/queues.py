from queue import Queue, LifoQueue

my_queue = Queue()
print(my_queue.empty())

my_queue.put(1)
my_queue.put("Hello")

print(my_queue.get())
print(my_queue.get())



# can be called a stack

my_lifo_queue = LifoQueue()
my_lifo_queue.put(1)
my_lifo_queue.put("Hello")

print(my_lifo_queue.get())
print(my_lifo_queue.get())
