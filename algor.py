# examples of algorithms in python shown below, used for studying
# to test
fruits = ['apple', 'banana', 'strawberries', 'blueberries', 'peaches', 'orange']

#comment out whatever i don't want to use for the sorting method

# BUBBLE SORT:
def bubble(a_list):
    swapped = True #initializing it, always assume it's true

    while swapped:
        swapped = False 

        for i in range (1, len(a_list)):
            if a_list[i-1] > a_list[i]:
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
                swapped = True

print(f"The fruit list before sorting: {fruits}") #to show
# apply the bubble sort
bubble(fruits)
print(f"The fruit list afterwards: {fruits}") # should provide the sorted list, using the code above

# INSERTION SORT
def in_sort(a_list):
    i = 1 
    while i < len(a_list):
        j = i
        while j > 0 and a_list[j-1] > a_list[j]:
            a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            j -= 1 # Move left
        i += 1 # Move to the next value

print(f"The fruit list before sorting: {fruits}") #to show
# apply the insertion sort
in_sort(fruits)
print(f"The fruit list afterwards: {fruits}") # should provide the sorted list, using the code above
