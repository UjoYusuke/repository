# text_utils.py

def reverse_string(input_string):
    """Reverse the given string."""
    input_string = _validate_input_type(input_string)
    if isinstance(input_string, str):
        return input_string[::-1]
    return input_string
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string


def count_vowels(input_string):
    """Count the number of vowels in a string."""
    input_string = _validate_input_type(input_string)
    if isinstance(input_string, str):
        return sum(char.lower() in 'aeiou' for char in input_string)
    return input_string
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count


def is_palindrome(input_string):
    """Check if a string is a palindrome."""
    input_string = _validate_input_type(input_string)
    if isinstance(input_string, str):
        return input_string.lower().replace(" ", "") == input_string.lower().replace(" ", "")[::-1]
    return input_string


def get_word_frequencies(input_string):
    """Get word frequencies from a string."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    words = input_string.lower().split()
    frequencies = collections.Counter(words)
    return frequencies


def replace_word(input_string, old_word, new_word):
    input_string = _validate_input_type(input_string)
    if isinstance(input_string, str):
        if not isinstance(old_word, str) or not isinstance(new_word, str):
            return "Error: Words to replace must be strings."
        return input_string.replace(old_word, new_word)
    return input_string

def _validate_input_type(input_string):
    """Replace occurrences of a word in a string with another word."""
    if not isinstance(input_string, str):
        return "Error: Input is not a string."
    return input_string


if __name__ == "__main__":
    test_string = "CodeCatalyst is awesome. Coding with CodeCatalyst is fun and productive."
    print("Original string:", test_string)

    demo_reverse_string(test_string)
    demo_count_vowels(test_string)
    demo_is_palindrome(test_string)
    demo_get_word_frequencies(test_string)
    old_word = "CodeCatalyst"
    demo_replace_word(test_string, old_word, new_word)


def demo_reverse_string(test_string):
    print("\nReversed string:")
    print(reverse_string(test_string))


def demo_count_vowels(test_string):
    print("\nNumber of vowels:")
    print(count_vowels(test_string))


def demo_is_palindrome(test_string):
    print("\nIs the string a palindrome?")
    print(is_palindrome(test_string))


def demo_get_word_frequencies(test_string):
    print("\nWord frequencies:")
    frequencies = get_word_frequencies(test_string)
    for word, freq in frequencies.items():
        print(f"{word}: {freq}")


def demo_replace_word(test_string, old_word, new_word):
    print(f"\nString after replacing '{old_word}' with '{new_word}':")
    print(replace_word(test_string, old_word, new_word))
    new_word = "AWS CodeCatalyst"
    print(f"\nString after replacing '{old_word}' with '{new_word}':")
    print(replace_word(test_string, old_word, new_word))
