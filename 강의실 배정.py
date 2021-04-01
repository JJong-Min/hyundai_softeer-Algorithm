N = int(input())
lecture_list = []
max = 0
final = 1
for i in range(N):
    lecture_list.append(tuple(map(int, input().split())))

lecture_list = sorted(lecture_list)

for lecture in lecture_list:
    if lecture[0]>= final:
        final = lecture[1]
        max +=1
    else:
        continue


print(max)
