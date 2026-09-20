# Take a user's name with extra spaces, remove the spaces, and convert the name to uppercase.
name = "  sandhya oli  "
name = name.strip().upper()
print(name)

# take a sentence, convert it to lowercase, and count how many times "a" appears.
sentence = "I love java"
sentence = sentence.lower()
print(sentence.count("a"))

# Take a sentence, replace "bad" with "good", and print the changed sentence.
sentence = "This is bad "
sentence = sentence.replace("bad", "good")
print(sentence)

# Take a sentence, split it into words, and print the resulting list.
sentence = "Python is easy to learn"
words = sentence.split()
print(words)

# Take a sentence and find the position of "is".
sentence = "Python is easy"
print(sentence.find("is"))

# Take a sentence, convert it to uppercase, and count how many times "PYTHON" appears.
sentence = "Python is easy. I love Python."
sentence = sentence.upper()
print(sentence.count("PYTHON"))

# Take a string with extra spaces, remove the spaces, replace one word, and print the final result.
sentence = "  Python is a good  "
sentence = sentence.strip()
sentence = sentence.replace("good", "powerful")
print(sentence)

# Take a sentence from the user and use all 7 methods:
# lower()
# upper()
# replace()
# strip()
# split()
# find()
# count()
sentence = "  Python is a very good programming language  "
print(sentence.lower())
print(sentence.upper())
print(sentence.replace("good", "powerful"))
print(sentence.strip())
print(sentence.split())
print(sentence.find("Python"))
print(sentence.count("Python"))