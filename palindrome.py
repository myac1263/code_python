# Find the largest palindrome made from the product of two 3-digit numbers
def palindrome_list(a_list):
    # If the list has only one element, it's obviously a palindrome
    if len(a_list) == 1:
        return True
    # If the list has 2 or 3 elements, check the first and last elements
    elif len(a_list) <= 3:
        return a_list[0] == a_list[-1]
    else:
        step = len(a_list) // 2
        j = len(a_list) - 1
        # Loop only up to the middle of the list to check for palindrome
        for i in range(0, step):
            if a_list[i] != a_list[j]:
                return False
            j -= 1
        return True

