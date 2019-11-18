"""
Given a string called text, e.g. text = 'This is a sentence'
Write a list comprehension (one line!) that produces a list of the words that have > 3 characters
print(long_words)
should output: ['This', 'Sentence']
"""

text = 'This is a sentence'
long_words = [char for char in text.split() if len(char) > 3]
print(long_words)
