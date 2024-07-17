import sys

numbers = set()
number = ''
while True:
    num = sys.stdin.read()
    print(num)
    if num.isnumeric():
        number += num
    # 둘다 빈 것이면 끝
    elif number == '':
        break
    else:
        nnumber = int(number)
        number = ''
        if nnumber not in numbers:
            print(nnumber, end=' ')
            numbers.add(nnumber)
