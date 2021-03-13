n = int(input())

results = []
count = 0
def hanoi(N, src, dest, transfer):
    if N == 1:
        return results.append([src, dest])
    hanoi(N-1, src, transfer, dest)
    results.append([src, dest])
    hanoi(N-1, transfer, dest, src)

hanoi(n,1,3,2)

print(len(results))

for result in results:
    print(result[0], result[1])