# return a list of factors, return the factors at k, location 3
# k = location 3
 
def find_factors(n, k):
    result = []
    for divider in range (1, n+1): # "n+1" can also be written as math.sqrt(n) -> from math import sqrt, int(n ** 0.5)
        if n % divider == 0:
            result.append(divider)

    if len(result) <= k-1:
        return -1
    else:
        return result[k-1]

