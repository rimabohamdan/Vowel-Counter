def count_vowel(string):
    vowels = "aeiou"
    return sum(string.lower().count(vowel) for vowel in vowels)

string = input("Enter a string: ")
result = count_vowel(string)
print(f"Number of vowels in the string: {result}")
