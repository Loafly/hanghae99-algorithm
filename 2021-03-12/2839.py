import sys

FIVE = 5
THREE = 3

sugar = int(sys.stdin.readline())

min_x = sugar // FIVE
min_y = (sugar - (FIVE * min_x)) // THREE

while True:
    if min_x * FIVE + min_y * THREE == sugar:
        print(min_x + min_y)
        break
    else:
        min_x -= 1
        min_y = (sugar - (FIVE * min_x)) // THREE

    if min_x == -1:
        print(-1)
        break