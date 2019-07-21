# _*_ coding=utf-8 _*_


import heapq
import random

# 使用内置堆排序模块,heapq.heappop(data)每次pop出一个最小的元素

data = [i for i in range(100)]
random.shuffle(data)
# 建立堆
heapq.heapify(data)
li = []
for i in range(len(data)):
    li.append(heapq.heappop(data))
print(li)
