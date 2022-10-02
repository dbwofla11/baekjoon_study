# 단어 정렬 
num = int(input())
words = []

for _ in range(num):
  word = input()
  words.append(word)

set_words = list(set(words))
new_words = []
for i in set_words:
  new_words.append((len(i) , i))

result = sorted(new_words)
for i ,word in result:
  print(word)
