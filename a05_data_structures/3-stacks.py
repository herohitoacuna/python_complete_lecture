from collections import deque

# ******************** STACKS ****************
# stack = resembles of stack of items in the real world.
# LIFO = last In First Out
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)             # [1, 2, 3]
last = browsing_session.pop()
print(last)                         # 3
print(browsing_session)             # [1, 2]
print("redirect", browsing_session[-1])  # redirect 2

if not browsing_session:           # not = Falsy, if browsing_session is = [] = Falsy, so Falsy and Falsy will result True
    print("disable")


# ******************** QUEUES ****************
# FIFO = First In First Out
# when dealing with a large item, its more efficient to use a "DEQUE" object
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
