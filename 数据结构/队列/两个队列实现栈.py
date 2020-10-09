from 队列 import Queue

q1 = Queue()
q2 = Queue()
for item in range(6):
    q1.enqueue(item)
while True:
    while q1.size() > 1:
        item = q1.dequeue()
        q2.enqueue(item)
    print(q1.dequeue())
    q1,q2 = q2,q1
    if q1.size() == 0:
        break

