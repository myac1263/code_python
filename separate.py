# Given a single string input where its words are separated by whitespaces, output each word within the string input individually.
# Example Input: “Hello World Poop Pee”
# Output:
# Hello
# World
# Poop
# Pee

sentence = input("Input your string here: ")
answer = sentence.split()
for word in answer:
    print(word)