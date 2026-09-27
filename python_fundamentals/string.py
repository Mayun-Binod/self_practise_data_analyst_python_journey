# Take a sentence from the user and convert it to uppercase.
sentence = "I am learning Python"
print(sentence.upper())

# Convert a sentence to lowercase.
sentence = "I AM LEARNING PYTHON"
print(sentence.lower())

# Replace spaces with -.
sentence = "I am learning Python"
print(sentence.replace(" ", "-"))

# Remove extra spaces using strip().
sentence = "   I am learning Python   "
print(sentence.strip())

# Split a sentence into words.
sentence = "I am learning Python"
words = sentence.split()
print(words)

# Find the position of a word using find().
sentence = "I am learning Python"
position = sentence.find("Python")
print(position)

# Count how many times a character appears using count().
sentence = "I am learning Python"
count = sentence.count("n")
print(count)