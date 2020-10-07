def findMedian(arr):
    arr.sort()
    return arr[int(len(arr) / 2)]
