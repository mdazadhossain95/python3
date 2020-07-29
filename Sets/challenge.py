# create a program that takes some text and returns a list of
# all the characters in the text that are not vowles, sorted in
# alphabetical order
#
# you can either enter the text from the keyboard or
# initialise a string variable with the string

sampleText = "python is a very powerful language"

vowels = frozenset("aeiou")
#vawels = { "a", "e", "i", "o", "u"}
fainalset = set(sampleText).difference(vowels)
print(fainalset)

fainalset = sorted(fainalset)
print(fainalset)








