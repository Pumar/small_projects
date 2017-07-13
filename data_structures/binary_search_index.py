def binary_search(a, target):
    """Your code goes here."""
    
    first = 0
    last = len(a)-1
    while (first<=last):
        i = (first+last)/2
        if a[i]==target:
            return i
        elif a[i]<target:
            first = i+1
        else:
            last = i -1
    return -1