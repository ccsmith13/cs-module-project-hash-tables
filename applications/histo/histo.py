# Your code here
import re

with open("robin.txt") as f:
    words = f.read()
    words = re.sub(r'\W+', ' ', words)
    words = words.lower().split()

cache={}
sorted_dict = dict()
results=[]

for word in words: 
    if word not in cache and word != '': 
        cache[word] = 1
    else:
        cache[word] += 1

cache = sorted(cache.items(), key=lambda x: (-x[1], x[0]))
print(cache)


