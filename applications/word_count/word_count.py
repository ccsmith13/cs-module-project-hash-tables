
excluded_chars = '":;,.-+=/\\|[]{}()*^&'

def word_count(s):
    # Your code here
    s = s.split()
    cache = {}
    for raw_word in s:
        word = raw_word.strip(excluded_chars).lower()
        if word is '': 
            return cache
        if word not in cache: 
            cache[word] = 0
        cache[word] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))