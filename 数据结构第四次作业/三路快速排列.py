import random
import time

def three_way_partition(arr, low, high):
    # 1. 随机选择pivot，交换到区间起点
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]

    # 2. 三路划分指针初始化
    lt = low  # [low, lt) < pivot
    gt = high  # (gt, high] > pivot
    i = low + 1  # 遍历指针

    # 3. 遍历划分
    while i <= gt:
        if arr[i] < pivot:
            # 小于pivot：交换到lt位置，lt和i右移
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            # 大于pivot：交换到gt位置，gt左移，i不变（需重新判断）
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            # 等于pivot：i右移，留在中间区间
            i += 1

    # 返回两个分界点：lt-1是< pivot的最后一个位置，gt+1是> pivot的第一个位置
    return lt - 1, gt + 1


def three_way_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 三路划分，得到两个分界点
        lt_end, gt_start = three_way_partition(arr, low, high)
        # 只递归排序< pivot和> pivot的区间，中间= pivot的部分已有序
        three_way_quicksort(arr, low, lt_end)
        three_way_quicksort(arr, gt_start, high)
    return arr


# 测试代码
if __name__ == "__main__":
    # 测试用例1：普通数组
    arr1 = [2, 34, 56, 3, 24, 53, 45, 35, 99, 87]
    print("三路快排-原数组: ", arr1)
    start = time.time()
    three_way_quicksort(arr1)
    end = time.time()
    print("三路快排-排序后: ", arr1)
    print(f"三路快排-耗时: {end - start:.6f}秒\n")

    # 测试用例2：大量重复元素数组（验证三路快排优势）
    arr2 = [5, 3, 5, 5, 2, 5, 7, 5, 5, 1, 5, 9, 5]
    print("三路快排-重复元素原数组: ", arr2)
    start = time.time()
    three_way_quicksort(arr2)
    end = time.time()
    print("三路快排-重复元素排序后: ", arr2)
    print(f"三路快排-重复元素耗时: {end - start:.6f}秒")