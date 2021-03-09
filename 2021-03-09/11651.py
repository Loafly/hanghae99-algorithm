length = int(input())
point_list = []

for i in range(0,length):
    x,y = input().split()
    point_list.append([int(x),int(y)])

point_list.sort(key=lambda x: (x[1], x[0]))

for i in range(0, len(point_list)):
    print(point_list[i][0], point_list[i][1])
