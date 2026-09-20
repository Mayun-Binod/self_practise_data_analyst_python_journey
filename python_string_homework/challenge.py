# Ask the user to enter a sentence. Clean the extra spaces, convert it to lowercase, count "python", find its position, replace "python" with "programming", and finally split the sentence into words.
sentence = "  Python is easy to learn Python is powerful  "
sentence = sentence.strip()
sentence = sentence.lower()
print(sentence.count("python"))
print(sentence.find("python"))
sentence = sentence.replace("python", "programming")
print(sentence)
words = sentence.split()
print(words)

# Ask the user to enter their full name with unnecessary spaces. Clean it, convert it to uppercase, and count how many times the letter "A" appears.
name = "  sandhya   oli  "
name = name.strip()
name = name.upper()
print(name)
print(name.count("a"))

# Ask the user to enter a sentence. Find a word entered by the user, count how many times it appears, and replace it with another word. solve this without input
sentence = "Python is easy. Python is powerful."
print(sentence.count("Python"))
sentence = sentence.replace("Python","Java")
print(sentence)



