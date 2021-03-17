import sys

def password_catch(string):
    


length = int(sys.stdin.readline())

for i in range(length):
    string = sys.stdin.readline()
    result = password_catch(string)
    print(result)



