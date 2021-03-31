N = int(input())
array = [0]*16
array[0] = 2
n = 1
while n<=N:
    array[n] = 2*array[n-1]-1
    n+=1

answer = array[N]*array[N]

print(answer)
