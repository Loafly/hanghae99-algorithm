#변수를 입력받는 방법
text = input()
alphabat_count = []

overlap_check = False
overlap_count_check = 0

for i in range(0, 26):
    alphabat_count.append(0)

for i in range(0, len(text)):
    # text_ascii = ord(text[i])
    # index = 0
    # #대문자
    # if text_ascii >= 65 and text_ascii <= 90:
    #     index = text_ascii - 65
    #     alphabat_count[index] += 1
    # #소문자
    # elif text_ascii >= 97 and text_ascii <= 122:
    #     index = text_ascii - 97
    #     alphabat_count[index] += 1
    
    text_ascii = ord(text[i].upper())
    index = 0
    index = text_ascii - 65
    alphabat_count[index] += 1

max_alphabat_count = max(alphabat_count)
max_alphabat_index = alphabat_count.index(max_alphabat_count)

for i in range(0,26):
    if alphabat_count[i] == alphabat_count[max_alphabat_index]:
        overlap_count_check += 1
    if overlap_count_check >= 2:
        overlap_check = True
        break

if overlap_check:
    print('?')
else:
    print(chr(65 + max_alphabat_index))


    

