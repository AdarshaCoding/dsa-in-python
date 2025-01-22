arr = [1, 2, 3, 4, 5, 6, 4, 6, 2]
k = 3


def max_sum(arr, k):
    w_sum = sum(arr[:k])  # 1+2+3 = 6
    m_sum = w_sum
    print(arr[:k])

    for i in range(k, len(arr)):
        w_sum = w_sum + arr[i] - arr[k - i]
        print(arr[i])
        m_sum = max(m_sum, w_sum)
    return m_sum


print(max_sum(arr, k))
