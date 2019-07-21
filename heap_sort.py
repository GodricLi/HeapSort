# _*_ coding=utf-8 _*_


import random

"""
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
    即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
1.大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
2.小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
堆排序的平均时间复杂度为 Ο(nlogn)。
算法步骤:
1.创建一个堆 H[0……n-1]；
2.把堆首（最大值）和堆尾互换；
3.把堆的尺寸缩小 1，并调用 sift()，目的是把列表数据调整到相应位置，构建成堆；
4.重复步骤 2，直到堆的尺寸为 1。
"""


def sift(li, low, high):
    """
    调整
    :param li:数据列表
    :param low:堆的根节点下标，
    :param high:堆的最后一个元素的下标
    :return:
    """
    i = low                                         # i最开始指向根节点
    j = 2 * i + 1                                   # j是i的左边子节点
    tmp = li[i]                                     # 将根的值保存
    while j <= high:                                # j存在值，能不超过最大下标
        if j + 1 <= high and li[j + 1] > li[j]:     # 右边的子节点存在且较大
            j = j + 1                               # j指向右边子节点
        if li[j] > tmp:                             # 左边子节点较大,调换位置
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:                                       # tmp较大,循环结束，tmp放到i的位置
            break
    li[i] = tmp                                     # j超过high，下一层没有元素了，tmp放到叶子节点


def heap_sort(li):
    """
    把堆首（最大值）和堆尾互换；
    :param li:
    :return:
    """
    n = len(li)
    sub_index = (n-2) // 2                          # 子节点的下标
    for i in range(sub_index, -1, -1):              # i表示建堆时需要调整的那部分的根下标
        sift(li, i, n-1)                            # 建堆完成
    for i in range(n-1, -1, -1):                    # i是最后一个元素
        li[0], li[i] = li[i], li[0]                 # 把堆首（最大值）和堆尾互换
        sift(li, 0, i-1)                            # i-1是首尾互换后最后的元素下标


data = [i for i in range(100)]
random.shuffle(data)
print(data)

if __name__ == '__main__':
    heap_sort(data)
    print(data)