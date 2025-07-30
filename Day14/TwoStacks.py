def twoStacks(maxSum, a, b):
    sum_ = 0
    i = 0
    j = 0
    maxCount = 0

    # Take as many as possible from stack a
    while i < len(a) and sum_ + a[i] <= maxSum:
        sum_ += a[i]
        i += 1

    maxCount = i

    # Now try taking from b and remove from a if needed
    while j < len(b) and i >= 0:
        sum_ += b[j]
        j += 1

        while sum_ > maxSum and i > 0:
            i -= 1
            sum_ -= a[i]

        if sum_ <= maxSum and (i + j) > maxCount:
            maxCount = i + j

    return maxCount
