n = int(input())

for i in range(n):
   words = input().split(' ')
   ordered_words = sorted(words, key=len, reverse=True)
   print(" ".join(ordered_words))
   