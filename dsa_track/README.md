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

3.  Abstract notion of Order Of Growth - O() - Big oh

    - Evaluate the algorithm
    - Evaluate scalability
    - Evaluate in terms of input size

    BEST CASE ➡ if the element found at first position
    WORST CASE ➡ if the element not found in the list
    AVERAGE CASE ➡ if the element found in the middle of the list

    ✔ Need to consider the worst case always to finalize

    ✔ Time is directly depends on the input provided to the program

    a. Evaluate the program's effeciency when **_input is very big_**
    b. Express/evaluate the **_growth of program's run time_** as input size grows
    c. Want to put an **_upper bound_** on growth - as tight as possible - To know the worst case
    d. Do not need to precise : "Order Of" not "Exact" growth
    e. Look at large factors in run time (which section of the program will take the longest to run?)

    ```
    # Count the opertions:  1 + 5n -> 5n -> n => O(n)
    def factorial(n):
    result = 1  # Op: 1
    while n > 1:  # Op: number of iterations
        result = result * n
        n = n - 1
    return result
    print(factorial(5))
    ```

    Examples:

    ```
    # remove the constant
    # remove multiplicant

    n**2 + 2n + 2 =>n**2 + 2n =>n**2 => O(n**2)
    n**2 + 100000n + 3**10000 => n**2 + 100000n => n**2 => O(n**2)
    log(n) + n + 4 => log(n) + n =>  n => n
    0.0001 * n * log(n) + 300n => n*(logn) + n => nlogn => O(nlogn)
    # polynomial or exponential
    2n**30 + 3**n => n**30 + 3**n  => 3**n => O(3**n)  ( 3**n > n**30)
    ```
