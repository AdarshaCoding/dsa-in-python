def findClosestNumber(nums):
    results = []
    for el in nums:
        results.append(abs(el + 0))
    print(min(results))


nums = [-4, -2, 1, 4, 8]
findClosestNumber(nums)
