# Sliding Window

**_Maximum sum of selected window elements _**

```python
    arr = [1, 2, 3, 4, 5] , k = 3
    n = len(arr) # length of the array
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[k-i]
        max_sum = max(max_sum, window_sum)
    return max_sum

```

- k = 3: the index starts from "0", so initial elements are 1, 2, 3 and its sum = 1+2+3 = 6
- keep two variables to tract the current window sum and maxmimum of current and previous window sums
- Start travel through the array elements after the current window, using for loop till end of the loop
- Add the next element value to current window and subtract/remove the first element from the previous window to have only 3 elements in current window.
-
