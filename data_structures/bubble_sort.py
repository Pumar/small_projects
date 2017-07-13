
def bubblesort(l):
    """
    Runtime: O(n^2)
    """
    last = len(l)-1
    for i in range(last):
        for j in range(i+1, last):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l