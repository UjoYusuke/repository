# text_utils.py

def reverse_string(input_string):
    """Reverse the given string."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string


def count_vowels(input_string):
    """Count the number of vowels in a string."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count


def is_palindrome(input_string):
    """Check if a string is a palindrome."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    normalized_string = input_string.lower().replace(" ", "")
    return normalized_string == normalized_string[::-1]


def get_word_frequencies(input_string):
    """Get word frequencies from a string."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    words = input_string.lower().split()
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies


def replace_word(input_string, old_word, new_word):
    """Replace occurrences of a word in a string with another word."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    if not isinstance(old_word, str) or not isinstance(new_word, str):
        return "Error: Words to replace must be strings."
    return input_string.replace(old_word, new_word)


if __name__ == "__main__":
    test_string = "CodeCatalyst is awesome. Coding with CodeCatalyst is fun and productive."

    print("Original string:", test_string)

    # Reverse the string
    print("\nReversed string:")
    print(reverse_string(test_string))

    # Count vowels
    print("\nNumber of vowels:")
    print(count_vowels(test_string))

    # Check if the string is a palindrome
    print("\nIs the string a palindrome?")
    print(is_palindrome(test_string))

    # Get word frequencies
    print("\nWord frequencies:")
    frequencies = get_word_frequencies(test_string)
    for word, freq in frequencies.items():
        print(f"{word}: {freq}")

    # Replace a word
    old_word = "CodeCatalyst"
    new_word = "AWS CodeCatalyst"
    print(f"\nString after replacing '{old_word}' with '{new_word}':")
    print(replace_word(test_string, old_word, new_word))
