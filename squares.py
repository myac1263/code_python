# import statments
from math import sqrt, floor

#input
titles = int(input()) #int() is a type casting function that converts its argument to integers

# processing

# answer = titles ** 0.5
answer = sqrt(titles)
answer = floor(answer)

#output
print(f"The largest square had a side length {answer}.")