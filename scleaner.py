# cleaner("H E L L 0O!") -> "hello"
# Function:
# 1 argument string

# Returns:
# 1 string object

# Functional Decomposition
# the function takes a single argument and return a string
# looks through each character of the string, grabs only alphabetical characters or removes non-alphacharacters
# grow an empty string to a string filled with alphabetical
# string method use: .isalpha() ... returns True if the string has only "letter" characters from the ASCII table

def string_cleaner(text):
    ''' to clean a string with no alpha characters and put them all in lowercased
    
    Arguments
        text : a string argument that is to be cleaned

    returns 
        a string object with only alphabetical lowercased character
    '''
    result = '' # initialiized an empty string
    for character in text:
        # print(character)
        if character.isalpha():
            result += character.lower()
            # .lower makes a string all lowercase
            # + operator is a concatenation operator to combine strings


    return result
# end of string_cleaner()

value = string_cleaner('HELL0, WORLD!')
print(f"Value is: {value}")