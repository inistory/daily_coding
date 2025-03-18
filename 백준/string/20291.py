#파일 정리
from collections import Counter

n = int(input())
file_list = []
for _ in range(n):
    file = input()
    file_list.append(file.split(".")[1])

counter = Counter(file_list)
sorted_counter = dict(sorted(counter.items()))

for ext, count in sorted_counter.items():
    print(f"{ext} {count}")
