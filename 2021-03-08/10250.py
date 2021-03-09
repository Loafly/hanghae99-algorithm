import math

#변수를 입력받는 방법
length = int(input())
hotels = []

for i in range(0,length):
     H,W,N = input().split()
     hotels.append([H,W,N])

for i in range(0,len(hotels)):
    hotel_H = int(hotels[i][0])
    hotel_X = int(hotels[i][1])
    client_count = int(hotels[i][2])

    client_x = int(client_count / hotel_H)
    client_y = hotel_H
    
    if client_count % hotel_H != 0:
        client_x += 1
        client_y = client_count % hotel_H    

    if len(str(client_x)) == 1:
        client_x = '0' + str(client_x)

    print(str(client_y) + str(client_x))
