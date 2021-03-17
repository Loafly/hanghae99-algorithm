import sys

scales = list(map(int, sys.stdin.readline().split()))

asc = True
desc = True

for i in range(len(scales)):
    if scales[i] != i + 1:
        asc = False
    if scales[len(scales) - i - 1] != i + 1:
        desc = False

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')

