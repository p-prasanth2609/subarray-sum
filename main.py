A=list(map(int,input().split()))
N=len(A)
result=0
for i in range(N):
    result += A[i] * (i + 1) * (N - i)

print(result)
