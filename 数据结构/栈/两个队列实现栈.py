from 栈 import Stack


s1 = Stack()
s2 = Stack()

for i in range(5):
    s1.push(i)

while s1.size() > 1:
    item = s1.pop()
    s2.push(item)
print(s1.pop())
while s2.size() > 0:
    print(s2.pop())