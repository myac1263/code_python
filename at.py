# Create a program that determines the index of the @ symbol from a given inputted string. 
# Assume that index starts at 0.
# 4a) Make the program stop as soon as it encounters an @ symbol it has reached the end ##linear search
# 4b) Make the program continue searching for the @ symbol to look for duplicates
# 4c) How would your solution change if the string was sorted? ##binary search, but linear search may be better
    #ANS: If the first value is larger than the ASCCI value of the @ symbol, then the @ symbol doesn't exist. If it does exist in this case, since it's sorted than binary search is preferred


## 4a)
text = input("Enter a sentence: ")
found = False
if not text:
    print("No @ symbol found")
elif len(text) == 1:
    if text[0] == "@":
        print("@ symbol at index 0")
    else:
        print("No @ symbol found")
else:
    1 = 0
    while i < len(text):
        if text[i] == "@":
            found = True
            break
        i += 1
    if found:
        print(f"@ symbol at index {1}")
    else:
        print("No @ symbol found")