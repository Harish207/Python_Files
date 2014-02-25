def is_prime(x):
    hits=0
    for i in range(1,x+1):
        if x % i == 0:
            hits += 1
    if hits == 2:
        return True
    else:
        return False