"""
words = ["level", "world", "deed", "hello", "noon", "python"]
# Expected Output: ['level', 'deed', 'noon'] → reversed → ['level', 'deed', 'noon']
polindroms = list(filter(lambda word: word[::-1] == word, words ))
print(polindroms)
polindroms  = [word[::-1] for word in polindroms]
print(polindroms)
"""

"""
nums = [10, 20, 55, 60, 75, 80, 95]
# Output: [3600, 6400]  # 60 and 80
chosen = list(filter(lambda num: num > 50 and num % 2 == 0, nums))
print(chosen)
chosen = list(map(lambda num: num ** 2, chosen))
print(chosen)
"""

"""
word1 = "programming"
word2 = "grammar"
# Output: ['g', 'r', 'a', 'm']
commo_lets = list(set(filter(lambda ch: ch in word2, word1)))
print(commo_lets)
"""

"""
data = [(3, 6), (2, 5), (4, 2), (9, 0), (7, 2)]
# Output: [18, 36]  # (3+6)=9, (9+0)=9 are divisible by 3 → 3*6 and 9*0

chosen = list(filter(lambda tuple: (tuple[0] + tuple[1]) % 3 == 0, data))
print(chosen)
chosen = list(map(lambda tuple: tuple[0] * tuple[1], chosen))
print(chosen)
"""

"""
from itertools import combinations
words = ["listen", "silent", "enlist", "inlets", "google", "goolge", "hello"]
# Output: [('listen', 'silent', 'enlist'), ('google', 'goolge', 'ooggle')]
combs = list(combinations(words, 3))
print(combs)
anagrams = list(filter(lambda comb: sorted(comb[0]) == sorted(comb[1]) == sorted(comb[2]), combs))
print(anagrams)
"""
"""
def with_music(func):
    def wrper():
        func()
        print("You will be with music, don't worry. I get that you like it")
    return wrper


@with_music
def run():
    print("You are going to start running. Are you ready?")


run()
"""

def log_function(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"Calling the function: {func.__name__}")
        print(f"Arguments : {args}")
    return wrapper


@log_function
def add(a, b):
    print( a + b)

print(add(5, 4))