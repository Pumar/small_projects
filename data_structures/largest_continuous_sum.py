def largest_continous(l):
    """
    Runtime: O(n)
    """
    max_sum = 0
    start = 0
    end = 1
    while (end < len(l)+1):
        if l[start] + l[start+1] > 0:
            curr_sum = sum(l[start:end])
            max_sum = max(curr_sum, max_sum)
            end += 1
        else:
            # Start new sequence
            start = end + 1
            end = start + 1
    return max_sum


k = [5,-2,6,-3,12,-24,-1,1,30,-5,-10,-2]
print largest_continous(k)