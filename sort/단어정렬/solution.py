n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))
words.sort() #알파벳 순
words.sort(key=len) #길이순

for word in words:
    print(word)