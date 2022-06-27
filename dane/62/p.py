number = 0
num=0
for num in range(10):
    print('Num is ' + str(num))
    if num == 5:
            break    # break here
    for number in range(10):
        if number == 5:
            break    # break here
        print('Number is ' + str(number))

print('Out of loop')