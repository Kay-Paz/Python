# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop.
# For instance, if s is a str, you could print each of its characters, one at a time, with code like:

# for c in s:
#     print(c, end="")

original_string = input("Input: ")

new_string = original_string.replace('A','').replace('a','').replace('E','').replace('e','').replace('I','').replace('i','').replace('O','').replace('o','').replace('U','').replace('u','')

print("Output: ",new_string)


