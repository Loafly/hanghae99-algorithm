#변수를 입력받는 방법
length = int(input())
average = []

for i in range(0, length):
    class_score = 0
    class_average = 0
    class_over_count = 0

    score = input().split()
    for j in (range(0, int(score[0]))):
        class_score += int(score[j + 1])

    class_average = class_score / int(score[0])

    for j in (range(0, int(score[0]))):
        if int(score[j + 1]) > class_average:
            class_over_count += 1
    # print(float(class_over_count))
    average.append((float(class_over_count) / float(score[0]) * 100))

for i in range(0, len(average)):
    print('%.3f' % average[i] + '%')