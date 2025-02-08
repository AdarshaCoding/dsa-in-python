# DSA in Python

### Techniques to measure time

1.  Measuring Time (using time) to execute
    - Different time for differnt algorithm (✔)
    - Time varies if implemention changes ex. for or while loop (❌)
    - Different machine different time due to RAM/Storage(❌)
    - Does not work for extremely small input(❌)
    - Time varies for different inputs but can't establish a relationship(❌)
2.  Counting Operations involved

    - Depends on the input, each operations will be counted

    ```
    def sum(x):
        total_sum = 0
        for i in range(x+1):
            total_sum = total_sum + x
        return total_sum
    print(sum(4)) #20
    ```

    - Different time for differnt algorithm (✔)
    - Time varies if implemention changes ex. for or while loop (❌)
    - Different machine different time due to RAM/Storage(✔)
    - No clear definition of which operation to count(❌)
    - Time varies for different inputs but can't establish a relationship(✔)

3.  Abstract notion of Order Of Growth

    - Evaluate the algorithm
    - Evaluate scalability
    - Evaluate in terms of input size

    BEST CASE ➡ if the element found at first position
    WORST CASE ➡ if the element not found in the list
    AVERAGE CASE ➡ if the element found in the middle of the list

    ➡ Need to consider the worst case always to finalize
