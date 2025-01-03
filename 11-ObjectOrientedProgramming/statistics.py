import math


class Statistics:
    def __init__(self, arr):
        self.arr = arr

    def add(self):
        num = int(input("Enter number"))
        self.arr.append(num)

    def display(self):
        print(" ".join(self.arr))

    def max(self):
        return max(self.arr)

    def min(self):
        return min(self.arr)

    def arith_mean(self):
        return sum(self.arr) / len(self.arr)

    def median(self):
        return sorted(self.arr)[math.floor(len(self.arr) / 2)]

    def overall(self):
        print(
            f"min: {self.min()}, max: {self.max()}, arithmetic: {self.arith_mean()}, median: {self.median()}"
        )


stat = Statistics([2, 34, 215, 4, 532, 53, 4])

stat.overall()
