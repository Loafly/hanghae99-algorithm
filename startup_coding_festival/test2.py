import sys
length = int(sys.stdin.readline())

for i in range(length):
    season_cupon, nomal_cupon = sys.stdin.readline().split()

    season_cupon = int(season_cupon)
    nomal_cupon = int(nomal_cupon)
    coffee_count = 0

    #둘다 0인경우
    if nomal_cupon == 0 and season_cupon == 0:
        print(coffee_count)
    #nomal_cupon이 0인경우
    elif nomal_cupon == 0:
        print(season_cupon // 12)
    #season_cupon이 5이하인 경우
    elif season_cupon < 5:
        print(coffee_count)
    #둘다 수가 있는 경우
    else:
        temp = season_cupon // 5
        temp1 = nomal_cupon // 7

        temp2 = min(temp,temp1)

        if temp2 != 0:
            coffee_count = temp2

            season_cupon = season_cupon - temp2 * 5
            nomal_cupon = nomal_cupon - temp2 * 7

        if season_cupon < 5:
            print(coffee_count)

        else:
            if season_cupon + nomal_cupon >= 12:
                if nomal_cupon <= 7:
                    season_cupon -= (12 - nomal_cupon)
                    nomal_cupon = 0
                    coffee_count += 1
                    coffee_count += season_cupon // 12
                else:
                    coffee_count += 1
                print(coffee_count)
            else:
                print(coffee_count)
            


