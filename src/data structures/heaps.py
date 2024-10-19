import heapq
from heapq import heappop, nlargest

my_list = [1,4,5,7,2,6,334,3456,2,5,3556,7,4,74,246,3]

heapq.heapify(my_list)

print(nlargest(1,my_list)[0])

while len(my_list) > 0:
    print(heappop(my_list))