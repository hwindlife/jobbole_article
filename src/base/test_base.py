import datetime
import time
import calendar
import random
from numba import jit
import numpy as np


num_loops = 5
len_of_list = 10000


def numpy_sort_test():
    img1 = np.ones((1000, 1000), np.int64) * 5
    img2 = np.ones((1000, 1000), np.int64) * 10
    img3 = np.ones((1000, 1000), np.int64) * 15
    start1 = time.time()
    for i in range(num_loops):
        result = add_arrays(img1, img2, img3)
    end1 = time.time()
    run_time1 = end1 - start1
    print('Average time for normal numpy operation={}'.format(run_time1 / num_loops))


def add_arrays(img1, img2, img3):
    return np.square(img1+img2+img3)


@jit(nopython=True)
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > cursor:
            # 从后往前对比，从小到大排序
            arr[pos] = arr[pos-1]
            pos = pos-1
        # 找到当前元素的位置
        arr[pos] = cursor
    return arr


def numba_sort_test():
    start = time.time()
    list_of_numbers = list()
    for i in range(len_of_list):
        num = random.randint(0, len_of_list)
        list_of_numbers.append(num)

    for i in range(num_loops):
        result = insertion_sort(list_of_numbers)

    end = time.time()

    run_time = end - start
    print('Average time={}'.format(run_time / num_loops))


def time_test():
    start = time.time()
    print(["开始：", start])

    print(time.localtime(time.time()))
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
    cal = calendar.month(2020, 2)
    print(cal)

    end = time.time()
    print(["结束：", end])
    print(["耗时：", end - start])


class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        """
        2820
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i, val in enumerate(nums):
            if i == nums_len - 1:
                break
            for j, val_scd in enumerate(nums[i+1:], i+1):
                if target == val + val_scd:
                    return [i, j]
        return []

    def twoSum1(self, nums: list, target: int) -> list:
        """
        5392
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len):
            if i == nums_len - 1:
                break
            for j in range(nums_len - i - 1):
                if target == nums[i] + nums[j + i + 1]:
                    return [i, j + i + 1]
        return []

    def twoSum2(self, nums: list, target: int) -> list:
        num2index = {}
        for i, j in enumerate(nums):
            if j in num2index:
                return [num2index.get(j), i]
            num2index[target - j] = i


if __name__ == '__main__':
    # img1 = np.ones((10, 10), np.int64) * 5
    # img2 = np.ones((1000, 1000), np.int64) * 10
    # print(img1)



    # numpy_sort_test()
    # numba_sort_test()
    # print(Solution().twoSum2([1, 2, 3], 8))

    # nums = [1, 2, 3]
    # for i, val in enumerate(nums, 1):
    #     print(val)

    print(np.arange(10, 30, 5))

