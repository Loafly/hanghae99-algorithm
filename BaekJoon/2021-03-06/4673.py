constructor = []
full_list = []

for i in (range(0,10001)):
    full_list.append(i)

for int_num in (range(0, 10001)):
    str_num = str(int_num)

    for i in (range(0, len(str_num))):
        int_num += int(str_num[i])

    # str_num = str(int_num)
    constructor.append(int_num)

complement = list(set(full_list) - set(constructor))

complement.sort()

for i in range(0, len(complement)):
    print(complement[i])