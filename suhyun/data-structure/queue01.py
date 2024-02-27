import queue

# 큐 모듈의 객체 선언
data = queue.Queue()
print(type(data))

data.put(2)
data.put(5)
data.put(8)

print(data.get())
print(data.get())
print(data.get())