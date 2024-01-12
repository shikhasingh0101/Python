def word_frequency(input_text):
    word_count = {}

    # Split the input text into words
    words = input_text.split()

    # Count the frequency of each word
    for word in words:
        word = word.lower()  # Convert to lowercase to treat words case-insensitively
        word_count[word] = word_count.get(word, 0) + 1

    # Sort the dictionary keys alphanumerically
    sorted_words = sorted(word_count.keys())

    # Output the frequency of each word
    for word in sorted_words:
        print(f"{word}: {word_count[word]}")

# Example usage:
input_text = "This is a simple example. Simple examples help in learning programming."
word_frequency(input_text)
