# 백준 2748번

n = int(input())
a = 0
b = 1
for i in range(n):
    a, b = b, a + b
print(a)
