t = int(input())
for _ in range(t):
   n, k = map(int, input().split())
   a = list(map(int, input().split()))
   b = Counter(a)
   result = []
   for key, value in b.items():
           result.append(key * value)
   result.sort(reverse=True)
   print(sum(result[0:k]))