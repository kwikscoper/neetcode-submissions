import bisect

class MedianFinder:

    def __init__(self):
        self.isEven = True
        self.n = 0
        self.arr = []

    def addNum(self, num: int) -> None:
        array = self.arr
        bisect.insort(array, num)
        self.isEven = not self.isEven
        self.n += 1

    def findMedian(self) -> float:
        array = self.arr
        halflist = int(self.n) // 2
        if self.isEven:
            return (array[halflist] + array[halflist - 1]) / 2.0
        else:
            return array[halflist] * 1.0