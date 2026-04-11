import random
import time

def randomized_partition(arr, low, high):
    # 1. 随机选择pivot
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    # 2. 标准partition过程
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 3. 放置pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low=0, high=None):
    # 给high设置默认值，调用时不用手动传len(arr)-1
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)
    return arr


# 测试代码
if __name__ == "__main__":
    # 把元组改成列表（元组不可修改，会报错）
    arr = [2, 34, 56, 3, 24, 53, 45, 35, 99, 87]
    print("原数组: ", arr)

    start = time.time()
    # 直接传数组即可，不用手动传0和len(arr)-1
    randomized_quicksort(arr)
    end = time.time()

    print("排序后: ", arr)
    print(f"耗时: {end - start:.6f}秒")