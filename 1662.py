def findString(arr):
    i = 0
    iback = 0
    length = 0
    isP = False
    while i < len(arr):
        # 괄호가 나오면
        if arr[i] == '(':
            isP = True
            # 뒤에 괄호 찾기
            frontCnt = 1
            backCnt = 0
            for j in range(i + 1, len(arr)):
                if arr[j] == '(':
                    frontCnt += 1
                elif arr[j] == ')':
                    backCnt += 1
                if frontCnt == backCnt:
                    back = j
                    break
            # 새로운 문자열
            length += len(arr[iback:i - 1]) + int(arr[i - 1]) * findString(arr[i + 1:back])
            # print(i, back)
            i = back + 1
            iback = i
        else:
            i += 1
    # print(newArr)
    # 괄호가 안나오면
    if isP == False:
        return len(arr)
    return length + len(arr) - iback

arr = list(input())

notReduced = findString(arr)
print(notReduced)
# print(len(notReduced))