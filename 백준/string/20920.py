from collections import Counter
import sys
input = sys.stdin.read

data = input().split()
n, m = int(data[0]), int(data[1])

words = data[2:]
filtered_words = [word for word in words if len(word) >= m]
word_count = Counter(filtered_words)

# 단어 빈도수 내림차순, 단어 길이 내림차순, 알파벳 사전 순으로 정렬
sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

for word, count in sorted_word_count:
    print(word)