import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    words = words.split()

# TODO: analyze which words can follow other words
# Your code here
cache = {}
curr_index = 0

for word in words: 
    if word not in cache: 
        if curr_index + 1 <= len(words)-1 :
            cache[word] = [words[curr_index+1]]
            curr_index += 1
        else: 
            cache[word] = ''
            curr_index += 1
    else: 
        if curr_index + 1 <= len(words)-1 :
            cache[word].append(words[curr_index+1])
            curr_index += 1

# TODO: construct 5 random sentences
# Your code here

current_word = random.choice(words)
result = []
while cache[current_word] != '':
    next_word = random.choice(cache[current_word])
    result.append(current_word)
    current_word = next_word

print (" ".join(result))
