def mean(a_list):
    # shorter way
    return sum(a_list) / len(a_list) # len() returns the length of x

def median(a_list):
    m = len(a_list) // 2 # let m be midpoint
    sorted_list = sorted(a_list) # can also do a_list.sort --> will mutate our a_list

    if len(a_list) % 2 == 0: 
        # length is even number of data points
        left = sorted_list [m-1]
        right = sorted_list [m]
        average = (left + right) / 2
        return average
    else:
        # length is odd
        return sorted_list [m]

# Testing
from random import seed
from random import randrange

seed(1)
data = [randrange(1,100) for _ in range(randrange(10,30))] # list comprehension
print(f'Our random detaset: {data}')
print(f'Our sorted dataset{sorted(data)}')
print(f'Mean of our dataset: {mean(data)}')
print(f'Median of our dataset: {median(data)}')