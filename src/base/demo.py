import numpy as np

if __name__ == "__main__":
    a = [1, 2, 3]
    b = np.array(a)
    c = np.array([[0, 1, 2, 10],
                  [12, 13, 100, 101],
                  [102, 110, 112, 113]], int)
    print(c)
    print(b)

    # 创建数值为1的数组
    # Numpy.ones(参数 1：shape，数组的形状；参数 2：dtype， 数值类型)
    array_one = np.ones([10, 10], dtype=np.int)
    print(array_one)

    # 创建数值为0的数组
    # Numpy.zeros(参数 1：shape，数组的形状；参数 2：dtype， 数值类型)
    array_zero = np.zeros([10, 9], dtype=np.float)
    print(array_zero)

    # 创建指定数值的数组
    # Numpy.full(参数 1：shape，数组的形状； 参数 2：constant value，数组填充的常数值；参数 3：dtype， 数值类型)
    array_full = np.full((2, 3), 5)
    print(array_full)

    # 创建单位矩阵
    # Numpy.eye(参数 1：N，方阵的维度)
    array_eye = np.eye(5)
    print(array_eye)

    # 创建对角矩阵
    # Numpy.diag(参数1：v，主对角线数值，参数 2：k，对角线元素)：K = 0表示主对角线，k>0的值选择在主对角线之上的对角线中的元素，k<0的值选择在主对角线之下的对角线中的元素
    array_diag = np.diag([10, 20, 30, 40], k = -2)
    print(array_diag)