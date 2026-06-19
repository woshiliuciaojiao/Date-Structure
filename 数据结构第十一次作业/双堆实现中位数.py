import heapq

class MedianFinder:
    def __init__(self):
        # 大顶堆：存储较小的一半元素（实际存储负数，利用 heapq 的小顶堆特性）
        self.max_heap = []   # 元素取负，堆顶是绝对值最大的负数（即原数最小的）
        # 小顶堆：存储较大的一半元素
        self.min_heap = []   # 正常存储，堆顶是最小元素

    def addNum(self, num: int) -> None:
        # 1. 先将新数加入大顶堆（较小的一半）
        heapq.heappush(self.max_heap, -num)
        # 2. 将大顶堆的最大值（即最小的负数）移到小顶堆，保证小顶堆中的元素都大于等于大顶堆
        #    此时大顶堆堆顶（负数）对应的原数是当前大顶堆中最大的，将其弹出并取反后加入小顶堆
        max_of_max_heap = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_of_max_heap)

        # 3. 平衡两堆大小：大顶堆的大小 >= 小顶堆的大小（相差不超过1）
        #    如果小顶堆比大顶堆多，则把小顶堆的最小值移到大顶堆
        if len(self.min_heap) > len(self.max_heap):
            min_of_min_heap = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_of_min_heap)

    def findMedian(self) -> float:
        # 如果两堆大小相等，中位数为两堆顶的平均值
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # 否则大顶堆比小顶堆多一个元素，中位数为大顶堆堆顶
        else:
            return -self.max_heap[0]

# 测试用例
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(3)
    print(mf.findMedian())  # 3.0
    mf.addNum(1)
    print(mf.findMedian())  # 2.0
    mf.addNum(4)
    print(mf.findMedian())  # 3.0
    mf.addNum(2)
    print(mf.findMedian())  # 2.5
    mf.addNum(5)
    print(mf.findMedian())  # 3.0