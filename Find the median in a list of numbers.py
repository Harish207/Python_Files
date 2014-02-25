def median(lst):
    median = 0.0
    lst = sorted(lst)
    index_even = len(lst)/2 - 1
    index_odd = round(len(lst)/2)-1
    if (len(lst)%2==0):
        median = (lst[index_even] + lst[(index_even + 1)]) / 2.0
    else:
        median = lst[index_odd]
    return median