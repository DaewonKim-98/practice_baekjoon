import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    password = str(input().strip())
    N = len(password)
    if password == 'end':
        break
    
    result = False
    for i in range(N):
        # 모음이 있으면
        if password[i] in vowel:
            result = True
        # 연속으로 모음이 3개 또는 자음이 3개 오면
        if N >= 3:
            if i + 2 < N:
                if password[i] in vowel and password[i + 1] in vowel and password[i + 2] in vowel:
                    result = False
                    break
                if password[i] not in vowel and password[i + 1] not in vowel and password[i + 2] not in vowel:
                    result = False
                    break
                
        # 같은 글자가 연속적으로 두번 오면
        if N >= 2:
            if i + 1 < N:
                if password[i] == password[i + 1] == 'e':
                    continue
                elif password[i] == password[i + 1] == 'o':
                    continue
                elif password[i] == password[i + 1]:
                    result = False
                    break
                    
                    
    
    if result == True:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
    