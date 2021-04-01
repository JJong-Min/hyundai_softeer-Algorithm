W, N = map(int, input().split())
treasure_list = []
cost = 0
for i in range(N):
    treasure_list.append(tuple(map(int, input().split())))

treasure_list = sorted(treasure_list, key = lambda treasure_list: treasure_list[1], reverse = True)

    
for treasure in treasure_list:
    if W == 0:
        break
    if W < treasure[0]:
        cost += W*treasure[1]
        W = 0
    else:
        cost += treasure[0]*treasure[1]
        W-=treasure[0]

print(cost)
