def array_sum(arr):
    sum = 0
    for item in arr:
        if isinstance(item, list):
            sum = sum + array_sum(item)
        else:
            sum = sum + item
    return sum