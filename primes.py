
size = int(input())
values = []
for i in range(size):
    values.append(int(input()))
    
def method1(num):
    counter = 0 
    for divider in range(1, num+1):
        if num % divider == 0:
            counter += 1
        return counter == 2

        