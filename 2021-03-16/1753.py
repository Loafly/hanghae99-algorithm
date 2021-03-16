import sys
V, E = sys.stdin.readline().split()
start_line = int(sys.stdin.readline())

line = {    

}

for i in range(int(E)):
    u,v,w = sys.stdin.readline().split()
    
    if u in line:
        line[u].appned([v,w])
    else:
        line[u] = [[v,w]]

    print(line)

# def DFS():

