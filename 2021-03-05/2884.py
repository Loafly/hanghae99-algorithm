#변수를 입력받는 방법
H,M = input().split()

#문자를 숫자로
H = int(H)
M = int(M)

#풀이
if M < 45 and M >= 0:
    if H < 24 and H > 0:
        H = H - int(1)
        M = int(60) + (M - int(45))
    elif H == int(0):
        H = 23
        M = int(60) + (M - int(45))        
elif M >= 45 and M < 60:
    M = M - int(45)
    
print(H,M)